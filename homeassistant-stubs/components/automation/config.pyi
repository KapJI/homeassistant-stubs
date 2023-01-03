from .const import CONF_ACTION as CONF_ACTION, CONF_HIDE_ENTITY as CONF_HIDE_ENTITY, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRACE as CONF_TRACE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import async_get_blueprints as async_get_blueprints
from _typeshed import Incomplete
from homeassistant.components import blueprint as blueprint
from homeassistant.components.trace import TRACE_CONFIG_SCHEMA as TRACE_CONFIG_SCHEMA
from homeassistant.config import config_without_domain as config_without_domain
from homeassistant.const import CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_ID as CONF_ID, CONF_VARIABLES as CONF_VARIABLES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, script as script
from homeassistant.helpers.condition import async_validate_conditions_config as async_validate_conditions_config
from homeassistant.helpers.trigger import async_validate_trigger_config as async_validate_trigger_config
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.yaml.input import UndefinedSubstitution as UndefinedSubstitution
from typing import Any

PACKAGE_MERGE_HINT: str
_CONDITION_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

async def _async_validate_config_item(hass: HomeAssistant, config: ConfigType, warn_on_errors: bool) -> AutomationConfig: ...

class AutomationConfig(dict):
    raw_config: Union[dict[str, Any], None]
    raw_blueprint_inputs: Union[dict[str, Any], None]

async def _try_async_validate_config_item(hass: HomeAssistant, config: dict[str, Any]) -> Union[AutomationConfig, None]: ...
async def async_validate_config_item(hass: HomeAssistant, config_key: str, config: dict[str, Any]) -> Union[AutomationConfig, None]: ...
async def async_validate_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
