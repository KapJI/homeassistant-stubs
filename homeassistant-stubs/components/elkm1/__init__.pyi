from .const import ATTR_KEY as ATTR_KEY, ATTR_KEYPAD_ID as ATTR_KEYPAD_ID, ATTR_KEY_NAME as ATTR_KEY_NAME, CONF_AREA as CONF_AREA, CONF_AUTO_CONFIGURE as CONF_AUTO_CONFIGURE, CONF_COUNTER as CONF_COUNTER, CONF_ENABLED as CONF_ENABLED, CONF_KEYPAD as CONF_KEYPAD, CONF_OUTPUT as CONF_OUTPUT, CONF_PLC as CONF_PLC, CONF_SETTING as CONF_SETTING, CONF_TASK as CONF_TASK, CONF_THERMOSTAT as CONF_THERMOSTAT, DISCOVERY_INTERVAL as DISCOVERY_INTERVAL, DISCOVER_SCAN_TIMEOUT as DISCOVER_SCAN_TIMEOUT, DOMAIN as DOMAIN, ELK_ELEMENTS as ELK_ELEMENTS, EVENT_ELKM1_KEYPAD_KEY_PRESSED as EVENT_ELKM1_KEYPAD_KEY_PRESSED, LOGIN_TIMEOUT as LOGIN_TIMEOUT
from .discovery import async_discover_device as async_discover_device, async_discover_devices as async_discover_devices, async_trigger_discovery as async_trigger_discovery, async_update_entry_from_discovery as async_update_entry_from_discovery
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, CONF_EXCLUDE as CONF_EXCLUDE, CONF_HOST as CONF_HOST, CONF_INCLUDE as CONF_INCLUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_PREFIX as CONF_PREFIX, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_USERNAME as CONF_USERNAME, CONF_ZONE as CONF_ZONE, Platform as Platform, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

SYNC_TIMEOUT: int
_LOGGER: Any
PLATFORMS: Any
SPEAK_SERVICE_SCHEMA: Any
SET_TIME_SERVICE_SCHEMA: Any

def _host_validator(config: dict[str, str]) -> dict[str, str]: ...
def _elk_range_validator(rng: str) -> tuple[int, int]: ...
def _has_all_unique_prefixes(value: list[dict[str, str]]) -> list[dict[str, str]]: ...

DEVICE_SCHEMA_SUBDOMAIN: Any
DEVICE_SCHEMA: Any
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, hass_config: ConfigType) -> bool: ...
def _async_find_matching_config_entry(hass: HomeAssistant, prefix: str) -> Union[ConfigEntry, None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _included(ranges: list[tuple[int, int]], set_to: bool, values: list[bool]) -> None: ...
def _find_elk_by_prefix(hass: HomeAssistant, prefix: str) -> Union[Elk, None]: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_wait_for_elk_to_sync(elk: Elk, login_timeout: int, sync_timeout: int) -> bool: ...
def _create_elk_services(hass: HomeAssistant) -> None: ...
def create_elk_entities(elk_data: dict[str, Any], elk_elements: list[Element], element_type: str, class_: Any, entities: list[ElkEntity]) -> Union[list[ElkEntity], None]: ...

class ElkEntity(Entity):
    _elk: Any
    _element: Any
    _mac: Any
    _prefix: Any
    _name_prefix: Any
    _temperature_unit: Any
    _unique_id: Any
    def __init__(self, element: Element, elk: Elk, elk_data: dict[str, Any]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
    def initial_attrs(self) -> dict[str, Any]: ...
    def _element_changed(self, element: Element, changeset: dict[str, Any]) -> None: ...
    def _element_callback(self, element: Element, changeset: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class ElkAttachedEntity(ElkEntity):
    @property
    def device_info(self) -> DeviceInfo: ...
