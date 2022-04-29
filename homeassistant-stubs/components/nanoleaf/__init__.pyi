import asyncio
from .const import DOMAIN as DOMAIN, NANOLEAF_EVENT as NANOLEAF_EVENT, TOUCH_GESTURE_TRIGGER_MAP as TOUCH_GESTURE_TRIGGER_MAP, TOUCH_MODELS as TOUCH_MODELS
from _typeshed import Incomplete
from aionanoleaf import EffectsEvent as EffectsEvent, Nanoleaf, StateEvent as StateEvent, TouchEvent as TouchEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
PLATFORMS: Incomplete

class NanoleafEntryData:
    device: Nanoleaf
    coordinator: DataUpdateCoordinator
    event_listener: asyncio.Task
    def __init__(self, device, coordinator, event_listener) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
