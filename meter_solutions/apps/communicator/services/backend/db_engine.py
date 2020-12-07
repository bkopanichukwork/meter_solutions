import json
import os
from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, Table, MetaData, select

from apps.communicator.services.backend import settings


DEVICE_ON = 1
DEVICE_OFF = 2
DEVICE_UNDEFINED = 3


def _save_data(device_id, indications_db, json_indications, meta, connection):
    """
        Saves all data from the device to the database.

        Parameter device_id - id of the device in the database
        Parameter indications_db - indications_db list of tuples (result of db query),
            each tuple contains id, measurement, designation of an indication that was sent by device
        Parameter json_indications - indications of the device as json
        Parameter data_table - Table for sqlalchemy to which function saves data
        Returns - none #TODO return status of the operation

    """
    data = Table(settings.DATA_TABLE, meta, autoload=True)

    logger.info("Preparing query with data:")
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

    insert_q = data.insert().values(prepared_data)
    insert_q.execute()


def _update_status(device_id, status, meta, connection):
    devices = Table(settings.DEVICES_TABLE, meta, autoload=True)

    if status == "ON":
        status = DEVICE_ON
    else:
        status = DEVICE_OFF

    device_update_query = devices.update() \
        .where(devices.c.id == device_id) \
        .values(status=status)

    connection.execute(device_update_query)

    logger.info(f"Status of the device with id {device_id} updated and setted to {status}")


def get_device_id_by_mqtt_id(device_mqtt_id, meta, connection):
    """
        Finds id of the device by its mqtt_id in database

            Parameter device_mqtt_id - mqtt id of the device
            Parameter meta - MetaData of the database
            Parameter connection - connection to the database
            Returns - device_id
    """
    devices = Table(settings.DEVICES_TABLE, meta, autoload=True)
    device_id_query = select([devices.c.id]). \
        where(devices.c.mqtt_id == device_mqtt_id).limit(1)
    device_id_result = list(connection.execute(device_id_query))

    device_id = device_id_result[0][0]

    logger.info(f"Found device id in table {settings.DATA_TABLE} - {device_id}")

    return device_id


def get_indications_info_by_measurement(indication_names, meta, connection):
    """
        Finds ids of indications in the database by their measurement

            Parameter measurements - mqtt id of the device
            Parameter meta - MetaData of the database
            Parameter connection - connection to the database
            Returns - list of tuples (result of db query),
                each tuple contains id, measurement, designation of an indication that was sent by device
    """
    indications = Table(settings.INDICATION_TABLE, meta, autoload=True)

    indications_query = select([indications.c.id,
                                indications.c.measurement,
                                indications.c.designation]). \
        where(indications.c.measurement.in_(indication_names))

    indications_result = list(connection.execute(indications_query))

    logger.info(f"Found info about indications in table {settings.INDICATION_TABLE} - {indications_result}")

    return indications_result


def json_to_database(json_indications, device_mqtt_id):
    """
        This function creates connection to the database collect all needed info
        and after that runs save_data function.
        #TODO - split to smaller functions

            Parameter json_indications - indications of a device as a json string
            Parameter device_mqtt_id - id of the device which sent this indications
            Returns - none #TODO return status of the operation
    """
    if not settings.DATABASE_URL:
        settings.DATABASE_URL = os.getenv("DATABASE_URL")

    db_engine = create_engine(settings.DATABASE_URL)

    meta = MetaData(db_engine)

    with db_engine.connect() as con:
        logger.info("Database connection established.")

        device_id = get_device_id_by_mqtt_id(device_mqtt_id, meta, con)

        json_indications = json.loads(json_indications)
        indication_names = [key for key in json_indications]
        indications_result = get_indications_info_by_measurement(indication_names, meta, con)

        _save_data(device_id, indications_result, json_indications, meta, con)

    db_engine.dispose()
    logger.info("Database connection closed.")


def device_status_to_database(status, device_mqtt_id):
    """
        This function updates devices status in the database

            Parameter status - ON / OFF
            Parameter device_mqtt_id - id of the device which sent this indications
            Returns - none #TODO return status of the operation
    """

    if not settings.DATABASE_URL:
        settings.DATABASE_URL = os.getenv("DATABASE_URL")

    db_engine = create_engine(settings.DATABASE_URL)

    meta = MetaData(db_engine)

    with db_engine.connect() as con:
        logger.info("Database connection established.")

        device_id = get_device_id_by_mqtt_id(device_mqtt_id, meta, con)

        _update_status(device_id, status, meta, con)

    db_engine.dispose()
    logger.info("Database connection closed.")
