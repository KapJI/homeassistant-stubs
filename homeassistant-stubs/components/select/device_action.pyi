from .const import ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, CONF_OPTION as CONF_OPTION, DOMAIN as DOMAIN, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import get_capability as get_capability
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ACTION_TYPES: Any
ACTION_SCHEMA: Any

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: dict, variables: dict, context: Union[Context, None]) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, Any]: ...
