from .const import DOMAIN as DOMAIN, LIVE_TV_APP_ID as LIVE_TV_APP_ID
from _typeshed import Incomplete
from aiowebostv import WebOsClient, WebOsTvState as WebOsTvState
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

_LOGGER: Incomplete
type WebOsTvConfigEntry = ConfigEntry[WebOsClient]

@callback
def async_get_device_entry_by_device_id(hass: HomeAssistant, device_id: str) -> DeviceEntry: ...
@callback
def async_get_device_id_from_entity_id(hass: HomeAssistant, entity_id: str) -> str: ...
@callback
def async_get_client_by_device_entry(hass: HomeAssistant, device: DeviceEntry) -> WebOsClient: ...
def get_sources(tv_state: WebOsTvState) -> list[str]: ...
def update_client_key(hass: HomeAssistant, entry: WebOsTvConfigEntry) -> None: ...
