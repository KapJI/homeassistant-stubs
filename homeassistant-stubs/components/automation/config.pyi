from .const import CONF_ACTION as CONF_ACTION, CONF_HIDE_ENTITY as CONF_HIDE_ENTITY, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRACE as CONF_TRACE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DOMAIN as DOMAIN
from .helpers import async_get_blueprints as async_get_blueprints
from _typeshed import Incomplete
from homeassistant.components import blueprint as blueprint
from homeassistant.components.device_automation.exceptions import InvalidDeviceAutomationConfig as InvalidDeviceAutomationConfig
from homeassistant.components.trace import TRACE_CONFIG_SCHEMA as TRACE_CONFIG_SCHEMA
from homeassistant.config import async_log_exception as async_log_exception, config_without_domain as config_without_domain
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_ID as CONF_ID, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, script as script
from homeassistant.helpers.condition import async_validate_conditions_config as async_validate_conditions_config
from homeassistant.helpers.trigger import async_validate_trigger_config as async_validate_trigger_config
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound
from typing import Any

PACKAGE_MERGE_HINT: str
_CONDITION_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_validate_config_item(hass: HomeAssistant, config: ConfigType, full_config: Union[ConfigType, None] = ...) -> Union[blueprint.BlueprintInputs, dict[str, Any]]: ...

class AutomationConfig(dict):
    raw_config: Union[dict[str, Any], None]

async def _try_async_validate_config_item(hass: HomeAssistant, config: dict[str, Any], full_config: Union[dict[str, Any], None] = ...) -> Union[AutomationConfig, blueprint.BlueprintInputs, None]: ...
async def async_validate_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
