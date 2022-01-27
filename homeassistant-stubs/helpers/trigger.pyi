from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from collections.abc import Callable as Callable
from homeassistant.const import CONF_ID as CONF_ID, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any

_PLATFORM_ALIASES: Any

async def _async_get_trigger_platform(hass: HomeAssistant, config: ConfigType) -> Any: ...
async def async_validate_trigger_config(hass: HomeAssistant, trigger_config: list[ConfigType]) -> list[ConfigType]: ...
async def async_initialize_triggers(hass: HomeAssistant, trigger_config: list[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool = ..., variables: TemplateVarsType = ...) -> Union[CALLBACK_TYPE, None]: ...
