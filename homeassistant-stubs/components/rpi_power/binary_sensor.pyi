from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rpi_bad_power import UnderVoltage as UnderVoltage
from typing import Any

_LOGGER: Any
DESCRIPTION_NORMALIZED: str
DESCRIPTION_UNDER_VOLTAGE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RaspberryChargerBinarySensor(BinarySensorEntity):
    _attr_device_class: Any
    _attr_icon: str
    _attr_name: str
    _attr_unique_id: str
    _under_voltage: Any
    def __init__(self, under_voltage: UnderVoltage) -> None: ...
    _attr_is_on: Any
    def update(self) -> None: ...
