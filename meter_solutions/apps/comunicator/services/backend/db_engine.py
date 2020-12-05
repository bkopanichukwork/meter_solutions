import contextlib
import json
import os
from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, Table, MetaData, select

from apps.comunicator.services.backend.device_handlers import settings


def save_data(device_id, indications_db, json_indications, data_table):
    logger.info("Preapring query with data:")
    logger.info(f"device_id - {device_id}")
    logger.info(f"indications_db - {indications_db}")
    logger.info(f"json_indications - {json_indications}")

    for key, value in json_indications.items():

        for indication_row in indications_db:
            if indication_row[1] == key:
                indication_id = indication_row[0]

        insert_q = data_table.insert().values(device_id=device_id,
                                              indication_id=indication_id,
                                              timestamp=datetime.now(),
                                              value=value)
        insert_q.execute()


def json_to_database(json_indications, device_id):
    if not settings.DATABASE_URL:
        settings.DATABASE_URL = os.getenv("DATABASE_URL")

    db_engine = create_engine(settings.DATABASE_URL)

    json_indications = json.loads(json_indications)
    indication_names = [key for key in json_indications]

    logger.info(indication_names)

    with db_engine.connect() as con:
        logger.info("Database connection established.")

        meta = MetaData(db_engine)

        indications = Table(settings.INDICATION_TABLE, meta, autoload=True)
        data = Table(settings.DATA_TABLE, meta, autoload=True)
        devices = Table(settings.DEVICES_TABLE, meta, autoload=True)

        devices = Table(settings.DEVICES_TABLE, meta, autoload=True)

        device_id_query = select([devices.c.id]). \
            where(devices.c.mqtt_id == device_id).limit(1)
        device_id_result = list(con.execute(device_id_query))

        logger.info(device_id_result)

        indications_query = select([indications.c.id,
                                    indications.c.measurement,
                                    indications.c.designation]). \
            where(indications.c.measurement.in_(indication_names))

        indications_result = list(con.execute(indications_query))
        logger.info(indications_result)

        save_data(device_id_result[0][0], indications_result, json_indications, data)

        con.close()
