from .const import CONF_CONNECTIONS as CONF_CONNECTIONS, CONF_COORDINATOR as CONF_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .model import EntityInfo as EntityInfo
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pyfritzhome import FritzhomeDevice as FritzhomeDevice
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class FritzBoxEntity(CoordinatorEntity):
    ain: Any
    _name: Any
    _unique_id: Any
    _unit_of_measurement: Any
    _device_class: Any
    _attr_state_class: Any
    def __init__(self, entity_info: EntityInfo, coordinator: DataUpdateCoordinator[dict[str, FritzhomeDevice]], ain: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> FritzhomeDevice: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
