from .const import CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_KNXKEY_FILENAME as CONF_KNX_KNXKEY_FILENAME, CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_LOCAL_IP as CONF_KNX_LOCAL_IP, CONF_KNX_MCAST_GRP as CONF_KNX_MCAST_GRP, CONF_KNX_MCAST_PORT as CONF_KNX_MCAST_PORT, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_ROUTE_BACK as CONF_KNX_ROUTE_BACK, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_ROUTING_BACKBONE_KEY as CONF_KNX_ROUTING_BACKBONE_KEY, CONF_KNX_ROUTING_SECURE as CONF_KNX_ROUTING_SECURE, CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE as CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_ID as CONF_KNX_SECURE_USER_ID, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TELEGRAM_LOG_SIZE as CONF_KNX_TELEGRAM_LOG_SIZE, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, CONF_KNX_TUNNELING_TCP_SECURE as CONF_KNX_TUNNELING_TCP_SECURE, CONF_KNX_TUNNEL_ENDPOINT_IA as CONF_KNX_TUNNEL_ENDPOINT_IA, KNX_ADDRESS as KNX_ADDRESS, TELEGRAM_LOG_DEFAULT as TELEGRAM_LOG_DEFAULT
from .device import KNXInterfaceDevice as KNXInterfaceDevice
from .expose import KNXExposeSensor as KNXExposeSensor, KNXExposeTime as KNXExposeTime
from .project import KNXProject as KNXProject
from .storage.config_store import KNXConfigStore as KNXConfigStore
from .telegrams import Telegrams as Telegrams
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx.core import XknxConnectionState
from xknx.core.telegram_queue import TelegramQueue as TelegramQueue
from xknx.dpt import DPTBase
from xknx.io import ConnectionConfig
from xknx.telegram import AddressFilter, Telegram as Telegram
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

_LOGGER: Incomplete

class KNXModule:
    hass: Incomplete
    config_yaml: Incomplete
    connected: bool
    exposures: list[KNXExposeSensor | KNXExposeTime]
    service_exposures: dict[str, KNXExposeSensor | KNXExposeTime]
    entry: Incomplete
    project: Incomplete
    config_store: Incomplete
    xknx: Incomplete
    telegrams: Incomplete
    interface_device: Incomplete
    _address_filter_transcoder: dict[AddressFilter, type[DPTBase]]
    group_address_transcoder: dict[DeviceGroupAddress, type[DPTBase]]
    knx_event_callback: TelegramQueue.Callback
    def __init__(self, hass: HomeAssistant, config: ConfigType, entry: ConfigEntry) -> None: ...
    async def start(self) -> None: ...
    async def stop(self, event: Event | None = None) -> None: ...
    def connection_config(self) -> ConnectionConfig: ...
    def connection_state_changed_cb(self, state: XknxConnectionState) -> None: ...
    def telegram_received_cb(self, telegram: Telegram) -> None: ...
    def register_event_callback(self) -> TelegramQueue.Callback: ...
