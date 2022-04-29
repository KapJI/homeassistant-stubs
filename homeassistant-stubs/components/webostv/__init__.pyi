from .const import ATTR_BUTTON as ATTR_BUTTON, ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_SOUND_OUTPUT as ATTR_SOUND_OUTPUT, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, SERVICE_BUTTON as SERVICE_BUTTON, SERVICE_COMMAND as SERVICE_COMMAND, SERVICE_SELECT_SOUND_OUTPUT as SERVICE_SELECT_SOUND_OUTPUT, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from _typeshed import Incomplete
from aiowebostv import WebOsClient
from collections.abc import Callable as Callable
from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Context as Context, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONFIG_SCHEMA: Incomplete
CALL_SCHEMA: Incomplete
BUTTON_SCHEMA: Incomplete
COMMAND_SCHEMA: Incomplete
SOUND_OUTPUT_SCHEMA: Incomplete
SERVICE_TO_METHOD: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_control_connect(host: str, key: Union[str, None]) -> WebOsClient: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class PluggableAction:
    _actions: Incomplete
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def async_attach(self, action: AutomationActionType, variables: dict[str, Any]) -> Callable[[], None]: ...
    def async_run(self, hass: HomeAssistant, context: Union[Context, None] = ...) -> None: ...

class WebOsClientWrapper:
    host: Incomplete
    client_key: Incomplete
    turn_on: Incomplete
    client: Incomplete
    def __init__(self, host: str, client_key: str) -> None: ...
    async def connect(self) -> None: ...
    async def shutdown(self) -> None: ...
