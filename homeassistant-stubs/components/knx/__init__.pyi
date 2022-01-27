from .const import CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_EXPOSE as CONF_KNX_EXPOSE, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, SUPPORTED_PLATFORMS as SUPPORTED_PLATFORMS
from .expose import KNXExposeSensor as KNXExposeSensor, KNXExposeTime as KNXExposeTime, create_knx_exposure as create_knx_exposure
from .schema import BinarySensorSchema as BinarySensorSchema, ButtonSchema as ButtonSchema, ClimateSchema as ClimateSchema, ConnectionSchema as ConnectionSchema, CoverSchema as CoverSchema, EventSchema as EventSchema, ExposeSchema as ExposeSchema, FanSchema as FanSchema, LightSchema as LightSchema, NotifySchema as NotifySchema, NumberSchema as NumberSchema, SceneSchema as SceneSchema, SelectSchema as SelectSchema, SensorSchema as SensorSchema, SwitchSchema as SwitchSchema, WeatherSchema as WeatherSchema, ga_validator as ga_validator, sensor_type_validator as sensor_type_validator
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final
from xknx.core import XknxConnectionState
from xknx.core.telegram_queue import TelegramQueue as TelegramQueue
from xknx.io import ConnectionConfig
from xknx.telegram import Telegram
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

_LOGGER: Any
CONF_KNX_FIRE_EVENT: Final[str]
CONF_KNX_EVENT_FILTER: Final[str]
SERVICE_KNX_SEND: Final[str]
SERVICE_KNX_ATTR_PAYLOAD: Final[str]
SERVICE_KNX_ATTR_TYPE: Final[str]
SERVICE_KNX_ATTR_RESPONSE: Final[str]
SERVICE_KNX_ATTR_REMOVE: Final[str]
SERVICE_KNX_EVENT_REGISTER: Final[str]
SERVICE_KNX_EXPOSURE_REGISTER: Final[str]
SERVICE_KNX_READ: Final[str]
CONFIG_SCHEMA: Any
SERVICE_KNX_SEND_SCHEMA: Any
SERVICE_KNX_READ_SCHEMA: Any
SERVICE_KNX_EVENT_REGISTER_SCHEMA: Any
SERVICE_KNX_EXPOSURE_REGISTER_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class KNXModule:
    hass: Any
    config: Any
    connected: bool
    exposures: Any
    service_exposures: Any
    entry: Any
    _address_filter_transcoder: Any
    _group_address_transcoder: Any
    _knx_event_callback: Any
    def __init__(self, hass: HomeAssistant, config: ConfigType, entry: ConfigEntry) -> None: ...
    xknx: Any
    def init_xknx(self) -> None: ...
    async def start(self) -> None: ...
    async def stop(self, event: Union[Event, None] = ...) -> None: ...
    def connection_config(self) -> ConnectionConfig: ...
    async def connection_state_changed_cb(self, state: XknxConnectionState) -> None: ...
    async def telegram_received_cb(self, telegram: Telegram) -> None: ...
    def register_event_callback(self) -> TelegramQueue.Callback: ...
    async def service_event_register_modify(self, call: ServiceCall) -> None: ...
    async def service_exposure_register_modify(self, call: ServiceCall) -> None: ...
    async def service_send_to_knx_bus(self, call: ServiceCall) -> None: ...
    async def service_read_to_knx_bus(self, call: ServiceCall) -> None: ...
