from . import DOMAIN as DOMAIN
from homeassistant.components.device_automation import toggle_entity as toggle_entity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

ACTION_SCHEMA: Any

async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context) -> None: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
