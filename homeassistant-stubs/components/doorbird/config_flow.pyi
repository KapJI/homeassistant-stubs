import voluptuous as vol
from .const import CONF_EVENTS as CONF_EVENTS, DEFAULT_DOORBELL_EVENT as DEFAULT_DOORBELL_EVENT, DEFAULT_MOTION_EVENT as DEFAULT_MOTION_EVENT, DOMAIN as DOMAIN, DOORBIRD_OUI as DOORBIRD_OUI
from .util import get_mac_address_from_door_station_info as get_mac_address_from_door_station_info
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
DEFAULT_OPTIONS: Incomplete
AUTH_VOL_DICT: VolDictType
AUTH_SCHEMA: Incomplete

def _schema_with_defaults(host: str | None = None, name: str | None = None) -> vol.Schema: ...
async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...
async def async_verify_supported_device(hass: HomeAssistant, host: str) -> bool: ...

class DoorBirdConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    reauth_entry: ConfigEntry
    discovery_schema: vol.Schema | None
    def __init__(self) -> None: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _async_validate_or_error(self, user_input: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
