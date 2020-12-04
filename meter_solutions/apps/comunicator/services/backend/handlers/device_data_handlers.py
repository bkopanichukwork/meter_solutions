import json
import os
from abc import abstractmethod

from loguru import logger
from sqlalchemy import create_engine, Table, select


class BaseDataHandler:

    @abstractmethod
    def decode_to_json(self, message):
        pass

    @abstractmethod
    def save_to_database(self, decoded):
        pass


class Zmai90DataHandler(BaseDataHandler):

    def __init__(self):
        logger.info("db_engine for Zmai90DataHandler created")
        self.db_engine = create_engine(os.getenv("DATABASE_URL"))

    def save_to_database(self, decoded):
        logger.info("Zmai90DataHandler save_to_database invoked")
        with self.db_engine.conncection() as con:
            logger.info("Database connection established.")
            indications = Table('meter_indication')
            stm = select([indications])
            rs = con.execute(stm)

            logger.info(rs.fetchall)

    def _decode_to_json(self, topic, message):
        topic_params = topic.split('/')
        device_model = topic_params[0].split('_')[0]
        device_id = topic_params[0].split('_')[1]

        if (topic_params[1] == "tele"):

            if (topic_params[2] == "LWT"):
                pass
            elif (topic_params[2] == "INFO1"):
                pass
            elif (topic_params[2] == "INFO2"):
                pass
            elif (topic_params[2] == "INFO3"):
                pass
            elif (topic_params[2] == "STATE"):
                pass
            elif (topic_params[2] == "RESULT"):
                pass

        elif (topic_params[1] == "stat"):
            pass

        return self.__decode(message)

    def __decode_param(self, payload, dimension):
        payload_len = len(payload)
        result = 0

        for i in reversed(range(0, payload_len + 1)):
            if i % 2 == 0:
                plyload_range = payload[i: i + 2]
                if plyload_range:
                    result = str(result) + plyload_range

        return float(result) / dimension

    def decode_to_json(self, message) -> str:
        # Decodes message from device to json
        result = {
            'consumedEnergy': self.__decode_param(message[6:14], 100),
            'voltage': self.__decode_param(message[14:22], 10),
            'current': self.__decode_param(message[22:30], 10000),
            'frequency': self.__decode_param(message[30:38], 100),
            'activePower': self.__decode_param(message[38:46], 100),
            'reactivePower': self.__decode_param(message[46:54], 100),
            'apparentPower': self.__decode_param(message[54:62], 100),
            'powerFactor': self.__decode_param(message[62:70], 10)
        }
        return json.dumps(result)

    @staticmethod
    def on_message(client, userdata, message):

        logger.info(f"Received {message}")
        logger.info(f"Message topic - {message.topic}")
        logger.info(f"Message payload - {message.payload}")

        msg = message.payload.decode("utf-8")
        msg = json.loads(msg)
        indications_encoded = msg['SerialReceived']

        handler = Zmai90DataHandler()
        indications_decoded = handler.decode_to_json(indications_encoded)

        logger.success(indications_decoded)

        handler.save_to_database(indications_decoded)
