from .const import CONF_DIM_MODE as CONF_DIM_MODE, CONF_SK_NUM_TRIES as CONF_SK_NUM_TRIES, DOMAIN as DOMAIN
from .helpers import purge_device_registry as purge_device_registry, purge_entity_registry as purge_entity_registry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete

def get_config_entry(hass: HomeAssistant, data: ConfigType) -> ConfigEntry | None: ...
async def validate_connection(host_name: str, data: ConfigType) -> ConfigType: ...

class LcnFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_import(self, data: ConfigType) -> ConfigFlowResult: ...
