import voluptuous as vol
from .const import DEFAULT_FAN_SPEED_AWAY as DEFAULT_FAN_SPEED_AWAY, DEFAULT_FAN_SPEED_BOOST as DEFAULT_FAN_SPEED_BOOST, DEFAULT_FAN_SPEED_HOME as DEFAULT_FAN_SPEED_HOME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, METRIC_KEY_PROFILE_FAN_SPEED_AWAY as METRIC_KEY_PROFILE_FAN_SPEED_AWAY, METRIC_KEY_PROFILE_FAN_SPEED_BOOST as METRIC_KEY_PROFILE_FAN_SPEED_BOOST, METRIC_KEY_PROFILE_FAN_SPEED_HOME as METRIC_KEY_PROFILE_FAN_SPEED_HOME, STATE_SCAN_INTERVAL as STATE_SCAN_INTERVAL
from _typeshed import Incomplete
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, NamedTuple
from uuid import UUID
from vallox_websocket_api import PROFILE as VALLOX_PROFILE, Vallox

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

class ValloxState:
    metric_cache: dict[str, Any]
    profile: VALLOX_PROFILE
    def get_metric(self, metric_key: str) -> StateType: ...
    @property
    def model(self) -> str | None: ...
    @property
    def sw_version(self) -> str: ...
    @property
    def uuid(self) -> UUID | None: ...
    def get_next_filter_change_date(self) -> date | None: ...
    def __init__(self, metric_cache, profile) -> None: ...

class ValloxDataUpdateCoordinator(DataUpdateCoordinator[ValloxState]): ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ValloxServiceHandler:
    _client: Incomplete
    _coordinator: Incomplete
    def __init__(self, client: Vallox, coordinator: DataUpdateCoordinator[ValloxState]) -> None: ...
    async def async_set_profile_fan_speed_home(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_away(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_boost(self, fan_speed: int = ...) -> bool: ...
    async def async_handle(self, call: ServiceCall) -> None: ...

class ValloxEntity(CoordinatorEntity[ValloxDataUpdateCoordinator]):
    _device_uuid: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator) -> None: ...
