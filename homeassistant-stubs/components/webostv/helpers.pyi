from .const import DOMAIN as DOMAIN, LIVE_TV_APP_ID as LIVE_TV_APP_ID
from aiowebostv import WebOsTvState as WebOsTvState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

@callback
def async_get_device_entry_by_device_id(hass: HomeAssistant, device_id: str) -> DeviceEntry: ...
@callback
def async_get_device_id_from_entity_id(hass: HomeAssistant, entity_id: str) -> str: ...
def get_sources(tv_state: WebOsTvState) -> list[str]: ...
