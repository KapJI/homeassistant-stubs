from . import ATTR_BRIGHTNESS_PCT as ATTR_BRIGHTNESS_PCT, ATTR_BRIGHTNESS_STEP_PCT as ATTR_BRIGHTNESS_STEP_PCT, DOMAIN as DOMAIN, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS
from homeassistant.components.device_automation import toggle_entity as toggle_entity
from homeassistant.components.light import ATTR_FLASH as ATTR_FLASH, FLASH_SHORT as FLASH_SHORT, SUPPORT_FLASH as SUPPORT_FLASH, VALID_BRIGHTNESS_PCT as VALID_BRIGHTNESS_PCT, VALID_FLASH as VALID_FLASH
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_DOMAIN as CONF_DOMAIN, CONF_TYPE as CONF_TYPE, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

TYPE_BRIGHTNESS_INCREASE: str
TYPE_BRIGHTNESS_DECREASE: str
TYPE_FLASH: str
ACTION_SCHEMA: Any

async def async_call_action_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType, context: Context) -> None: ...
async def async_get_actions(hass: HomeAssistant, device_id: str) -> list[dict]: ...
async def async_get_action_capabilities(hass: HomeAssistant, config: dict) -> dict: ...
