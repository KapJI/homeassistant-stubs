from .const import CONF_KNX_EXPOSE as CONF_KNX_EXPOSE, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, SupportedPlatforms as SupportedPlatforms
from .expose import KNXExposeSensor as KNXExposeSensor, KNXExposeTime as KNXExposeTime, create_knx_exposure as create_knx_exposure
from .schema import BinarySensorSchema as BinarySensorSchema, ClimateSchema as ClimateSchema, ConnectionSchema as ConnectionSchema, CoverSchema as CoverSchema, ExposeSchema as ExposeSchema, FanSchema as FanSchema, LightSchema as LightSchema, NotifySchema as NotifySchema, NumberSchema as NumberSchema, SceneSchema as SceneSchema, SelectSchema as SelectSchema, SensorSchema as SensorSchema, SwitchSchema as SwitchSchema, WeatherSchema as WeatherSchema, ga_validator as ga_validator, sensor_type_validator as sensor_type_validator
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final
from xknx.core.telegram_queue import TelegramQueue as TelegramQueue
from xknx.io import ConnectionConfig
from xknx.telegram import Telegram

_LOGGER: Any
CONF_KNX_FIRE_EVENT: Final[str]
CONF_KNX_EVENT_FILTER: Final[str]
SERVICE_KNX_SEND: Final[str]
SERVICE_KNX_ATTR_PAYLOAD: Final[str]
SERVICE_KNX_ATTR_TYPE: Final[str]
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

class KNXModule:
    hass: Any
    config: Any
    connected: bool
    exposures: Any
    service_exposures: Any
    _knx_event_callback: Any
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    xknx: Any
    def init_xknx(self) -> None: ...
    async def start(self) -> None: ...
    async def stop(self, event: Event) -> None: ...
    def connection_config(self) -> ConnectionConfig: ...
    def connection_config_routing(self) -> ConnectionConfig: ...
    def connection_config_tunneling(self) -> ConnectionConfig: ...
    async def telegram_received_cb(self, telegram: Telegram) -> None: ...
    def register_callback(self) -> TelegramQueue.Callback: ...
    async def service_event_register_modify(self, call: ServiceCall) -> None: ...
    async def service_exposure_register_modify(self, call: ServiceCall) -> None: ...
    async def service_send_to_knx_bus(self, call: ServiceCall) -> None: ...
    async def service_read_to_knx_bus(self, call: ServiceCall) -> None: ...
