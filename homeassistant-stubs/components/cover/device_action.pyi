import voluptuous as vol
from . import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, DOMAIN as DOMAIN, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_CLOSE_TILT as SUPPORT_CLOSE_TILT, SUPPORT_OPEN as SUPPORT_OPEN, SUPPORT_OPEN_TILT as SUPPORT_OPEN_TILT, SUPPORT_SET_POSITION as SUPPORT_SET_POSITION, SUPPORT_SET_TILT_POSITION as SUPPORT_SET_TILT_POSITION, SUPPORT_STOP as SUPPORT_STOP
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_TYPE as CONF_TYPE, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

CMD_ACTION_TYPES: Incomplete
POSITION_ACTION_TYPES: Incomplete
CMD_ACTION_SCHEMA: Incomplete
POSITION_ACTION_SCHEMA: Incomplete
ACTION_SCHEMA: Incomplete

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: ConfigType) -> dict[str, vol.Schema]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Union[Context, None]) -> None: ...
