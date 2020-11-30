import json
import sys
from abc import abstractmethod

from loguru import logger

from . import device_data_handlers
from . import device_managers


class DeviceHandlerNotFound(BaseException):
    pass


HANDLERS_LIST = {
    'zmai90': 'Zmai90DataHandler',
    'device5': 'Device5Handler',
}

MANAGERS_LIST = {
    'zmai90': 'Zmai90DeviceManager',
    'device5': 'Device5Manager',
}


def _get_device_handler_or_manager(device_model: str, is_manager: bool = False):
    """
        Returns class that can handle data from devices with given model
        or can manage status of such devices.
        If is_manager = False result will be a class that derived
        from BaseDataHandler and have methods that can decode data from device
        and save it to database.
        Otherwise it will be a class that derived from BaseDeviceManager and have
        methods to send commands to a device with device_model model.

        This method can raise DeviceHandlerNotFound exception
        in case if there is no such class or it isn`t defined in
        HANDLERS_LIST or MANAGERS_LIST.

        Parameters:
            device_model (str): device model name
            is_manager (bool): if True - returns device manager,
                otherwise data handler
    """

    LIST = HANDLERS_LIST
    handlers_list = device_data_handlers
    if is_manager:
        LIST = MANAGERS_LIST
        handlers_list = device_managers

    try:
        handler_name = LIST[device_model]
    except KeyError:
        error_str = f"No handler defined in dictionary"
        logger.error(error_str)
        raise DeviceHandlerNotFound(error_str)
    else:
        logger.info(f"Found handler with name {handler_name} in dictionary for {device_model} model")

    try:
        handler_class = getattr(handlers_list, handler_name)
    except AttributeError:
        error_str = f"No handler class {handler_name} for {device_model} model defined"
        logger.error(error_str)
        raise DeviceHandlerNotFound(error_str)
    else:
        logger.info(f"Found handler class {handler_class} for {device_model} model")
        return handler_class


def get_device_manager(device_model: str):
    """
        Wrapper for _get_device_handler_or_manager method.
    """
    return _get_device_handler_or_manager(device_model, True)


def get_device_data_handler(device_model: str):
    """
        Wrapper for _get_device_handler_or_manager method.
    """
    return _get_device_handler_or_manager(device_model, False)