import voluptuous as vol
from .const import DEFAULT_FAN_SPEED_AWAY as DEFAULT_FAN_SPEED_AWAY, DEFAULT_FAN_SPEED_BOOST as DEFAULT_FAN_SPEED_BOOST, DEFAULT_FAN_SPEED_HOME as DEFAULT_FAN_SPEED_HOME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import NamedTuple
from vallox_websocket_api import Vallox

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: list[str]
ATTR_PROFILE_FAN_SPEED: str
SERVICE_SCHEMA_SET_PROFILE_FAN_SPEED: Incomplete

class ServiceMethodDetails(NamedTuple):
    method: str
    schema: vol.Schema

SERVICE_SET_PROFILE_FAN_SPEED_HOME: str
SERVICE_SET_PROFILE_FAN_SPEED_AWAY: str
SERVICE_SET_PROFILE_FAN_SPEED_BOOST: str
SERVICE_TO_METHOD: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ValloxServiceHandler:
    _client: Incomplete
    _coordinator: Incomplete
    def __init__(self, client: Vallox, coordinator: ValloxDataUpdateCoordinator) -> None: ...
    async def async_set_profile_fan_speed_home(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_away(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_boost(self, fan_speed: int = ...) -> bool: ...
    async def async_handle(self, call: ServiceCall) -> None: ...

class ValloxEntity(CoordinatorEntity[ValloxDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _device_uuid: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator) -> None: ...
