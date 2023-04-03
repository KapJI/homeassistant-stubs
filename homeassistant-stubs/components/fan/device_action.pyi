from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_automation import toggle_entity as toggle_entity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType

ACTION_SCHEMA: Incomplete

async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict[str, str]]: ...
async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context | None) -> None: ...
