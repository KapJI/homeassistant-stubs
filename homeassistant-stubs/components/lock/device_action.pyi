from . import DOMAIN as DOMAIN, SUPPORT_OPEN as SUPPORT_OPEN
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from typing import Any

ACTION_TYPES: Any
ACTION_SCHEMA: Any

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: dict, variables: dict, context: Union[Context, None]) -> None: ...
