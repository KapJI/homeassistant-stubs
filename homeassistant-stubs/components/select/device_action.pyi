import voluptuous as vol
from .const import ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, CONF_OPTION as CONF_OPTION, DOMAIN as DOMAIN, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import get_capability as get_capability
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

ACTION_TYPES: Incomplete
ACTION_SCHEMA: Incomplete

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Union[Context, None]) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
