from .const import CONF_EVENTS as CONF_EVENTS, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .device import ConfiguredDoorBird as ConfiguredDoorBird
from .models import DoorBirdData as DoorBirdData
from .view import DoorBirdRequestView as DoorBirdRequestView
from _typeshed import Incomplete
from doorbirdpy import DoorBird
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
CONF_CUSTOM_URL: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _init_door_bird_device(device: DoorBird) -> tuple[tuple[bool, int], dict[str, Any]]: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_register_events(hass: HomeAssistant, door_station: ConfiguredDoorBird) -> bool: ...
async def _update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def _async_import_options_from_data_if_missing(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
