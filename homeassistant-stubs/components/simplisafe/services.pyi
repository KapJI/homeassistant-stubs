from . import SimpliSafeConfigEntry as SimpliSafeConfigEntry
from .const import ATTR_ALARM_DURATION as ATTR_ALARM_DURATION, ATTR_ALARM_VOLUME as ATTR_ALARM_VOLUME, ATTR_CHIME_VOLUME as ATTR_CHIME_VOLUME, ATTR_ENTRY_DELAY_AWAY as ATTR_ENTRY_DELAY_AWAY, ATTR_ENTRY_DELAY_HOME as ATTR_ENTRY_DELAY_HOME, ATTR_EXIT_DELAY_AWAY as ATTR_EXIT_DELAY_AWAY, ATTR_EXIT_DELAY_HOME as ATTR_EXIT_DELAY_HOME, ATTR_LIGHT as ATTR_LIGHT, ATTR_VOICE_PROMPT_VOLUME as ATTR_VOICE_PROMPT_VOLUME, DOMAIN as DOMAIN
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service, verify_domain_control as verify_domain_control
from typing import Any

ATTR_PIN_LABEL: str
ATTR_PIN_LABEL_OR_VALUE: str
ATTR_PIN_VALUE: str
VOLUME_MAP: Incomplete
SERVICE_NAME_REMOVE_PIN: str
SERVICE_NAME_SET_PIN: str
SERVICE_NAME_SET_SYSTEM_PROPERTIES: str
SERVICE_REMOVE_PIN_SCHEMA: Incomplete
SERVICE_SET_PIN_SCHEMA: Incomplete
SERVICE_SET_SYSTEM_PROPERTIES_SCHEMA: Incomplete
_verify_domain_control: Incomplete

@callback
def _async_get_system_for_service_call(call: ServiceCall) -> SystemType: ...
@callback
def extract_system(func: Callable[[ServiceCall, SystemType], Coroutine[Any, Any, None]]) -> Callable[[ServiceCall], Coroutine[Any, Any, None]]: ...
@_verify_domain_control
@extract_system
async def async_remove_pin(call: ServiceCall, system: SystemType) -> None: ...
@_verify_domain_control
@extract_system
async def async_set_pin(call: ServiceCall, system: SystemType) -> None: ...
@_verify_domain_control
@extract_system
async def async_set_system_properties(call: ServiceCall, system: SystemType) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
