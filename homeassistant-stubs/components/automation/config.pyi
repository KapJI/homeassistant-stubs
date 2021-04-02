from .const import CONF_ACTION as CONF_ACTION, CONF_HIDE_ENTITY as CONF_HIDE_ENTITY, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DOMAIN as DOMAIN
from .helpers import async_get_blueprints as async_get_blueprints
from homeassistant.components import blueprint as blueprint
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.config import async_log_exception as async_log_exception, config_without_domain as config_without_domain
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_ID as CONF_ID, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, script as script
from homeassistant.helpers.condition import async_validate_condition_config as async_validate_condition_config
from homeassistant.helpers.trigger import async_validate_trigger_config as async_validate_trigger_config
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound
from typing import Any, Optional

_CONDITION_SCHEMA: Any
PLATFORM_SCHEMA: Any

async def async_validate_config_item(hass: Any, config: Any, full_config: Optional[Any] = ...): ...

class AutomationConfig(dict):
    raw_config: Any = ...

async def _try_async_validate_config_item(hass: Any, config: Any, full_config: Optional[Any] = ...): ...
async def async_validate_config(hass: Any, config: Any): ...
