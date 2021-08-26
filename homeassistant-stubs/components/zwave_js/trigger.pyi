from .triggers import value_updated as value_updated
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from types import ModuleType
from typing import Any, Callable

TRIGGERS: Any

def _get_trigger_platform(config: ConfigType) -> ModuleType: ...
async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: Callable, automation_info: dict[str, Any]) -> Callable: ...
