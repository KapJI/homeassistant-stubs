from .const import LOGGER as LOGGER
from .entity import RememberTheMilkEntity as RememberTheMilkEntity
from .storage import RememberTheMilkConfiguration as RememberTheMilkConfiguration
from _typeshed import Incomplete
from homeassistant.components import configurator as configurator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
CONF_SHARED_SECRET: str
RTM_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_CREATE_TASK: str
SERVICE_COMPLETE_TASK: str
SERVICE_SCHEMA_CREATE_TASK: Incomplete
SERVICE_SCHEMA_COMPLETE_TASK: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _create_instance(hass: HomeAssistant, account_name: str, api_key: str, shared_secret: str, token: str, stored_rtm_config: RememberTheMilkConfiguration, component: EntityComponent[RememberTheMilkEntity]) -> None: ...
def _register_new_account(hass: HomeAssistant, account_name: str, api_key: str, shared_secret: str, stored_rtm_config: RememberTheMilkConfiguration, component: EntityComponent[RememberTheMilkEntity]) -> None: ...
