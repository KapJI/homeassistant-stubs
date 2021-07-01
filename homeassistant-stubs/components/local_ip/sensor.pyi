from .const import DOMAIN as DOMAIN, SENSOR as SENSOR
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import get_local_ip as get_local_ip
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPSensor(SensorEntity):
    _attr_unique_id: Any
    _attr_icon: str
    _attr_name: Any
    def __init__(self, name: str) -> None: ...
    _attr_state: Any
    def update(self) -> None: ...
