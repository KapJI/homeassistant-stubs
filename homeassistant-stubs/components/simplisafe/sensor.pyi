from . import SimpliSafeBaseSensor as SimpliSafeBaseSensor
from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimplisafeFreezeSensor(SimpliSafeBaseSensor, SensorEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    _attr_state: Any
    def async_update_from_rest_api(self) -> None: ...
