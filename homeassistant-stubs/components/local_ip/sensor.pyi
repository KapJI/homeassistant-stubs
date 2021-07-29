from .const import DOMAIN as DOMAIN, SENSOR as SENSOR
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.components.network.const import PUBLIC_TARGET_IP as PUBLIC_TARGET_IP
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPSensor(SensorEntity):
    _attr_unique_id: Any
    _attr_icon: str
    _attr_name: Any
    def __init__(self, name: str) -> None: ...
    _attr_state: Any
    async def async_update(self) -> None: ...
