from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType, HomeAssistantType as HomeAssistantType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from types import MappingProxyType
from typing import Any, Callable, Dict, List, Optional, Union

async def async_validate_trigger_config(hass: HomeAssistantType, trigger_config: List[ConfigType]) -> List[ConfigType]: ...
async def async_initialize_triggers(hass: HomeAssistantType, trigger_config: List[ConfigType], action: Callable, domain: str, name: str, log_cb: Callable, home_assistant_start: bool=..., variables: Optional[Union[Dict[str, Any], MappingProxyType]]=...) -> Optional[CALLBACK_TYPE]: ...
