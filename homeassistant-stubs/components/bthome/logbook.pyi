from .const import BTHOME_BLE_EVENT as BTHOME_BLE_EVENT, BTHomeBleEvent as BTHomeBleEvent, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import async_get as async_get
from homeassistant.helpers.typing import EventType as EventType

def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[EventType[BTHomeBleEvent]], dict[str, str]]], None]) -> None: ...
