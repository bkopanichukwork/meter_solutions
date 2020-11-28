import json

HANDLERS = {
    'zmai90': 'Zmai90DataHandler',
    'device2': 'Device2Handler',
    'device3': 'Device3Handler',
    'device4': 'Device4Handler',
    'device5': 'Device5Handler',
}

class Handler():

    def handle(self, topic, message):
        handler = getattr(HANDLERS, topic.split('_')[0])
        return handler()


class Zmai90DataHandler():
    def handle(self, topic, message):
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

    def __decode_param(self, payload, demension):
        payload_len = len(payload)
        result = 0

        for i in reversed(range(0, payload_len + 1)):
            if i % 2 == 0:
                plyload_range = payload[i: i + 2]
                if plyload_range:
                    result = str(result) + plyload_range

        return float(result) / demension

    def __decode(self, message) -> str:
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
