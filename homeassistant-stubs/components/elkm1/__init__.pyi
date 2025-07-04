from .const import ATTR_KEY as ATTR_KEY, ATTR_KEYPAD_ID as ATTR_KEYPAD_ID, ATTR_KEYPAD_NAME as ATTR_KEYPAD_NAME, ATTR_KEY_NAME as ATTR_KEY_NAME, CONF_AREA as CONF_AREA, CONF_AUTO_CONFIGURE as CONF_AUTO_CONFIGURE, CONF_COUNTER as CONF_COUNTER, CONF_KEYPAD as CONF_KEYPAD, CONF_OUTPUT as CONF_OUTPUT, CONF_PLC as CONF_PLC, CONF_SETTING as CONF_SETTING, CONF_TASK as CONF_TASK, CONF_THERMOSTAT as CONF_THERMOSTAT, DISCOVERY_INTERVAL as DISCOVERY_INTERVAL, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, ELK_ELEMENTS as ELK_ELEMENTS, EVENT_ELKM1_KEYPAD_KEY_PRESSED as EVENT_ELKM1_KEYPAD_KEY_PRESSED, LOGIN_TIMEOUT as LOGIN_TIMEOUT
from .discovery import async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_trigger_discovery as async_trigger_discovery, async_update_entry_from_discovery as async_update_entry_from_discovery
from .models import ELKM1Data as ELKM1Data
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_ENABLED as CONF_ENABLED, CONF_EXCLUDE as CONF_EXCLUDE, CONF_HOST as CONF_HOST, CONF_INCLUDE as CONF_INCLUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_PREFIX as CONF_PREFIX, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_USERNAME as CONF_USERNAME, CONF_ZONE as CONF_ZONE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.network import is_ip_address as is_ip_address

type ElkM1ConfigEntry = ConfigEntry[ELKM1Data]
SYNC_TIMEOUT: int
_LOGGER: Incomplete
PLATFORMS: Incomplete

def hostname_from_url(url: str) -> str: ...
def _host_validator(config: dict[str, str]) -> dict[str, str]: ...
def _elk_range_validator(rng: str) -> tuple[int, int]: ...
def _has_all_unique_prefixes(value: list[dict[str, str]]) -> list[dict[str, str]]: ...

DEVICE_SCHEMA_SUBDOMAIN: Incomplete
DEVICE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, hass_config: ConfigType) -> bool: ...
@callback
def _async_find_matching_config_entry(hass: HomeAssistant, prefix: str) -> ConfigEntry | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ElkM1ConfigEntry) -> bool: ...
def _included(ranges: list[tuple[int, int]], set_to: bool, values: list[bool]) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ElkM1ConfigEntry) -> bool: ...
async def async_wait_for_elk_to_sync(elk: Elk, login_timeout: int, sync_timeout: int) -> bool: ...
