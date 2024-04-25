from .const import CONF_ADDR as CONF_ADDR, CONF_CONTROLLER_ID as CONF_CONTROLLER_ID, CONF_DIMMERS as CONF_DIMMERS, CONF_KEYPADS as CONF_KEYPADS, CONF_RATE as CONF_RATE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, dispatcher_send as dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import slugify as slugify
from pyhomeworks.pyhomeworks import Homeworks
from typing import Any

_LOGGER: Incomplete
PLATFORMS: list[Platform]
CONF_COMMAND: str
EVENT_BUTTON_PRESS: str
EVENT_BUTTON_RELEASE: str
DEFAULT_FADE_RATE: float
KEYPAD_LEDSTATE_POLL_COOLDOWN: float
CV_FADE_RATE: Incomplete
DIMMER_SCHEMA: Incomplete
KEYPAD_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_SEND_COMMAND_SCHEMA: Incomplete

@dataclass
class HomeworksData:
    controller: Homeworks
    controller_id: str
    keypads: dict[str, HomeworksKeypad]
    def __init__(self, controller, controller_id, keypads) -> None: ...

def async_setup_services(hass: HomeAssistant) -> None: ...
async def async_send_command(hass: HomeAssistant, data: Mapping[str, Any]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def calculate_unique_id(controller_id: str, addr: str, idx: int) -> str: ...

class HomeworksEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _addr: Incomplete
    _idx: Incomplete
    _controller_id: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _controller: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, controller: Homeworks, controller_id: str, addr: str, idx: int, name: str | None) -> None: ...

class HomeworksKeypad:
    _addr: Incomplete
    _controller: Incomplete
    _debouncer: Incomplete
    _hass: Incomplete
    _name: Incomplete
    _id: Incomplete
    unsubscribe: Incomplete
    def __init__(self, hass: HomeAssistant, controller: Homeworks, controller_id: str, addr: str, name: str) -> None: ...
    def _update_callback(self, msg_type: str, values: list[Any]) -> None: ...
    def _request_keypad_led_states(self) -> None: ...
    async def request_keypad_led_states(self) -> None: ...
