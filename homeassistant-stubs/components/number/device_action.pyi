from . import DOMAIN as DOMAIN, const as const
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from typing import Any

ATYP_SET_VALUE: str
ACTION_SCHEMA: Any

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: dict, variables: dict, context: Union[Context, None]) -> None: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
