import json
import os
from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, Table, MetaData, select

from apps.communicator.services.backend import settings


def save_data(device_id, indications_db, json_indications, data_table):
    """
        Saves all data from the device to the database.

        Parameter device_id - id of the device in the database
        Parameter indications_db - indications_db list of tuples (result of db query),
            each tuple contains id, measurement, designation of an indication that was sent by device
        Parameter json_indications - indications of the device as json
        Parameter data_table - Table for sqlalchemy to which function saves data
        Returns - none #TODO return status of the operation

    """
    logger.info("Preapring query with data:")
    logger.info(f"device_id - {device_id}")
    logger.info(f"indications_db - {indications_db}")
    logger.info(f"json_indications - {json_indications}")

    prepared_data = list()
    for indication_measurement, indication_value in json_indications.items():

        for indication_row in indications_db:
            if indication_row[1] == indication_measurement:
                indication_id = indication_row[0]

        prepared_data.append({
                              "device_id": device_id,
                              "indication_id": indication_id,
                              "timestamp": datetime.now(),
                              "value": indication_value,
                              })

        insert_q = data_table.insert().values(prepared_data)
        insert_q.execute()


def json_to_database(json_indications, device_mqtt_id):
    """
        This function creates connection to the database
        finds ids of indications by their measurement,
        id of the device by its mqtt_id,
        and after that runs save_data function.
        #TODO - split to smaller functions

            Parameter json_indications - indications of a device as a json string
            Parameter device_id - id of the device which sent this indications
            Returns - none #TODO return status of the operation
    """
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

        device_id_query = select([devices.c.id]). \
            where(devices.c.mqtt_id == device_mqtt_id).limit(1)
        device_id_result = list(con.execute(device_id_query))

        logger.info(f"Found device id in table {settings.DATA_TABLE} - {device_id_result}")

        indications_query = select([indications.c.id,
                                    indications.c.measurement,
                                    indications.c.designation]). \
            where(indications.c.measurement.in_(indication_names))

        indications_result = list(con.execute(indications_query))
        logger.info(f"Found info about indications in table {settings.INDICATION_TABLE} - {indications_result}")

        save_data(device_id_result[0][0], indications_result, json_indications, data)

    db_engine.dispose()
    logger.info("Database connection closed.")

