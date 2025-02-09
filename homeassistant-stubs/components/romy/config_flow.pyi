from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo

class RomyConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str
    password: str
    robot_name_given_by_user: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_password(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _async_step_finish_config(self) -> ConfigFlowResult: ...
