from .const import CONF_API_ENABLED as CONF_API_ENABLED, CONF_PATH as CONF_PATH, CONF_PRODUCT_NAME as CONF_PRODUCT_NAME, CONF_PRODUCT_TYPE as CONF_PRODUCT_TYPE, CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import onboarding as onboarding, zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homewizard_energy.models import Device as Device
from typing import Any, NamedTuple

_LOGGER: Incomplete

class DiscoveryData(NamedTuple):
    ip: str
    product_name: str
    product_type: str
    serial: str

class HomeWizardConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery: DiscoveryData
    entry: ConfigEntry | None
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    @staticmethod
    async def _async_try_connect(ip_address: str) -> Device: ...

class RecoverableError(HomeAssistantError):
    error_code: Incomplete
    def __init__(self, message: str, error_code: str) -> None: ...
