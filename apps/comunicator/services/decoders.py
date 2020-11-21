import json


class Decoder:
    pass


class Zmai90Decoder(Decoder):

    def __decode_param(self, payload, demension):
        payload_len = len(payload)
        result = 0

        for i in reversed(range(0, payload_len + 1)):
            if i % 2 == 0:
                plyload_range = payload[i: i + 2]
                if plyload_range:
                    result = str(result) + plyload_range

        return float(result) / demension

    def decode(self, message) -> str:
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
