from .const import ADMIN_SERVICES as ADMIN_SERVICES, ALL_KEYS as ALL_KEYS, ATTR_UNIQUE_ID as ATTR_UNIQUE_ID, CONF_UNAUTHENTICATED_MODE as CONF_UNAUTHENTICATED_MODE, CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_NOTIFY_SERVICE_NAME as DEFAULT_NOTIFY_SERVICE_NAME, DOMAIN as DOMAIN, KEY_DEVICE_BASIC_INFORMATION as KEY_DEVICE_BASIC_INFORMATION, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_DIALUP_MOBILE_DATASWITCH as KEY_DIALUP_MOBILE_DATASWITCH, KEY_LAN_HOST_INFO as KEY_LAN_HOST_INFO, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, KEY_WLAN_HOST_LIST as KEY_WLAN_HOST_LIST, KEY_WLAN_WIFI_FEATURE_SWITCH as KEY_WLAN_WIFI_FEATURE_SWITCH, NOTIFY_SUPPRESS_TIMEOUT as NOTIFY_SUPPRESS_TIMEOUT, SERVICE_CLEAR_TRAFFIC_STATISTICS as SERVICE_CLEAR_TRAFFIC_STATISTICS, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_RESUME_INTEGRATION as SERVICE_RESUME_INTEGRATION, SERVICE_SUSPEND_INTEGRATION as SERVICE_SUSPEND_INTEGRATION, UPDATE_SIGNAL as UPDATE_SIGNAL
from .utils import get_device_macs as get_device_macs
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RECIPIENT as CONF_RECIPIENT, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery, entity_registry as entity_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, dispatcher_send as dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from typing import Any, Callable

_LOGGER: Any
SCAN_INTERVAL: Any
NOTIFY_SCHEMA: Any
CONFIG_SCHEMA: Any
SERVICE_SCHEMA: Any
CONFIG_ENTRY_PLATFORMS: Any

class Router:
    hass: HomeAssistant
    config_entry: ConfigEntry
    connection: Connection
    url: str
    data: dict[str, Any]
    subscriptions: dict[str, set[str]]
    inflight_gets: set[str]
    client: Client
    suspended: Any
    notify_last_attempt: float
    def __attrs_post_init__(self) -> None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def device_identifiers(self) -> set[tuple[str, str]]: ...
    @property
    def device_connections(self) -> set[tuple[str, str]]: ...
    def _get_data(self, key: str, func: Callable[[], Any]) -> None: ...
    def update(self) -> None: ...
    def logout(self) -> None: ...
    def cleanup(self, *_: Any) -> None: ...
    def __init__(self, hass, config_entry, connection, url, data, subscriptions, inflight_gets, suspended, notify_last_attempt) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class HuaweiLteData:
    hass_config: ConfigType
    config: dict[str, dict[str, Any]]
    routers: dict[str, Router]
    def __init__(self, hass_config, config, routers) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class HuaweiLteBaseEntity(Entity):
    router: Router
    _available: bool
    _unsub_handlers: list[Callable]
    @property
    def _entity_name(self) -> str: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _async_maybe_update(self, config_entry_unique_id: str) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def __init__(self, router, available, unsub_handlers) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
