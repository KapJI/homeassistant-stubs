from .const import ATTRIBUTION as ATTRIBUTION, CONF_POLLING as CONF_POLLING, DEFAULT_CACHEDB as DEFAULT_CACHEDB, DOMAIN as DOMAIN, LOGGER as LOGGER
from abodepy import Abode, AbodeAutomation as AbodeAuto
from abodepy.devices import AbodeDevice as AbodeDev
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DATE as ATTR_DATE, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_TIME as ATTR_TIME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import entity as entity
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from typing import Any

SERVICE_SETTINGS: str
SERVICE_CAPTURE_IMAGE: str
SERVICE_TRIGGER_AUTOMATION: str
ATTR_DEVICE_NAME: str
ATTR_DEVICE_TYPE: str
ATTR_EVENT_CODE: str
ATTR_EVENT_NAME: str
ATTR_EVENT_TYPE: str
ATTR_EVENT_UTC: str
ATTR_SETTING: str
ATTR_USER_NAME: str
ATTR_APP_TYPE: str
ATTR_EVENT_BY: str
ATTR_VALUE: str
CONFIG_SCHEMA: Any
CHANGE_SETTING_SCHEMA: Any
CAPTURE_IMAGE_SCHEMA: Any
AUTOMATION_SCHEMA: Any
PLATFORMS: Any

class AbodeSystem:
    abode: Any
    polling: Any
    entity_ids: Any
    logout_listener: Any
    def __init__(self, abode: Abode, polling: bool) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def setup_hass_services(hass: HomeAssistant) -> None: ...
async def setup_hass_events(hass: HomeAssistant) -> None: ...
def setup_abode_events(hass: HomeAssistant) -> None: ...

class AbodeEntity(entity.Entity):
    _attr_attribution: Any
    _data: Any
    _attr_should_poll: Any
    def __init__(self, data: AbodeSystem) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_available: Any
    def _update_connection_status(self) -> None: ...

class AbodeDevice(AbodeEntity):
    _device: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, data: AbodeSystem, device: AbodeDev) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def update(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def device_info(self) -> entity.DeviceInfo: ...
    def _update_callback(self, device: AbodeDev) -> None: ...

class AbodeAutomation(AbodeEntity):
    _automation: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_extra_state_attributes: Any
    def __init__(self, data: AbodeSystem, automation: AbodeAuto) -> None: ...
    def update(self) -> None: ...
