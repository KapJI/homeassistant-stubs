from .const import CONF_ALLOW_CLIP_SENSOR as CONF_ALLOW_CLIP_SENSOR, CONF_ALLOW_DECONZ_GROUPS as CONF_ALLOW_DECONZ_GROUPS, CONF_ALLOW_NEW_DEVICES as CONF_ALLOW_NEW_DEVICES, CONF_MASTER_GATEWAY as CONF_MASTER_GATEWAY, DEFAULT_ALLOW_CLIP_SENSOR as DEFAULT_ALLOW_CLIP_SENSOR, DEFAULT_ALLOW_DECONZ_GROUPS as DEFAULT_ALLOW_DECONZ_GROUPS, DEFAULT_ALLOW_NEW_DEVICES as DEFAULT_ALLOW_NEW_DEVICES, HASSIO_CONFIGURATION_URL as HASSIO_CONFIGURATION_URL, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .deconz_event import DeconzAlarmEvent as DeconzAlarmEvent, DeconzEvent as DeconzEvent
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from pydeconz import DeconzSession
from pydeconz.alarm_system import AlarmSystem as DeconzAlarmSystem
from pydeconz.group import Group as DeconzGroup
from pydeconz.light import DeconzLight as DeconzLight
from pydeconz.sensor import DeconzSensor as DeconzSensor
from types import MappingProxyType
from typing import Any

class DeconzGateway:
    hass: Any
    config_entry: Any
    api: Any
    available: bool
    ignore_state_updates: bool
    signal_reachable: Any
    signal_new_group: Any
    signal_new_light: Any
    signal_new_scene: Any
    signal_new_sensor: Any
    deconz_resource_type_to_signal_new_device: Any
    deconz_ids: Any
    entities: Any
    events: Any
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: DeconzSession) -> None: ...
    @property
    def bridgeid(self) -> str: ...
    @property
    def host(self) -> str: ...
    @property
    def master(self) -> bool: ...
    @property
    def option_allow_clip_sensor(self) -> bool: ...
    @property
    def option_allow_deconz_groups(self) -> bool: ...
    @property
    def option_allow_new_devices(self) -> bool: ...
    def async_connection_status_callback(self, available: bool) -> None: ...
    def async_add_device_callback(self, resource_type: str, device: Union[DeconzAlarmSystem, DeconzGroup, DeconzLight, DeconzSensor, list[Union[DeconzAlarmSystem, DeconzGroup, DeconzLight, DeconzSensor]], None] = ..., force: bool = ...) -> None: ...
    async def async_update_device_registry(self) -> None: ...
    @staticmethod
    async def async_config_entry_updated(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def options_updated(self) -> None: ...
    def shutdown(self, event: Event) -> None: ...
    async def async_reset(self) -> bool: ...

def get_gateway_from_config_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> DeconzGateway: ...
async def get_deconz_session(hass: HomeAssistant, config: MappingProxyType[str, Any]) -> DeconzSession: ...
