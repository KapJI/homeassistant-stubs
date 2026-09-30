from .const import DOMAIN as DOMAIN, LEDIrDeviceType as LEDIrDeviceType
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from infrared_protocols.codes.generic.led import BaseGenericLEDCode as BaseGenericLEDCode

CODES: dict[LEDIrDeviceType, type[BaseGenericLEDCode]]

class LEDIrBaseEntity(Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _codes: Incomplete
    _entry: Incomplete
    def __init__(self, entry: ConfigEntry, device_type: LEDIrDeviceType) -> None: ...
