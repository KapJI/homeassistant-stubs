from .const import CONF_KNX_AUTOMATIC as CONF_KNX_AUTOMATIC, CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_DEFAULT_RATE_LIMIT as CONF_KNX_DEFAULT_RATE_LIMIT, CONF_KNX_DEFAULT_STATE_UPDATER as CONF_KNX_DEFAULT_STATE_UPDATER, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_KNXKEY_FILENAME as CONF_KNX_KNXKEY_FILENAME, CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_LOCAL_IP as CONF_KNX_LOCAL_IP, CONF_KNX_MCAST_GRP as CONF_KNX_MCAST_GRP, CONF_KNX_MCAST_PORT as CONF_KNX_MCAST_PORT, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_ROUTE_BACK as CONF_KNX_ROUTE_BACK, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_ID as CONF_KNX_SECURE_USER_ID, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, CONF_KNX_TUNNELING_TCP_SECURE as CONF_KNX_TUNNELING_TCP_SECURE, CONST_KNX_STORAGE_KEY as CONST_KNX_STORAGE_KEY, DOMAIN as DOMAIN, KNXConfigEntryData as KNXConfigEntryData
from .schema import ia_validator as ia_validator, ip_v4_validator as ip_v4_validator
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import selector as selector
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from typing import Any, Final
from xknx.io.gateway_scanner import GatewayDescriptor as GatewayDescriptor

CONF_KNX_GATEWAY: Final[str]
CONF_MAX_RATE_LIMIT: Final[int]
CONF_DEFAULT_LOCAL_IP: Final[str]
DEFAULT_ENTRY_DATA: Incomplete
CONF_KNX_TUNNELING_TYPE: Final[str]
CONF_KNX_LABEL_TUNNELING_TCP: Final[str]
CONF_KNX_LABEL_TUNNELING_TCP_SECURE: Final[str]
CONF_KNX_LABEL_TUNNELING_UDP: Final[str]
CONF_KNX_LABEL_TUNNELING_UDP_ROUTE_BACK: Final[str]
_IA_SELECTOR: Incomplete
_IP_SELECTOR: Incomplete
_PORT_SELECTOR: Incomplete

class FlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _found_tunnels: list[GatewayDescriptor]
    _selected_tunnel: Union[GatewayDescriptor, None]
    _tunneling_config: Union[KNXConfigEntryData, None]
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> KNXOptionsFlowHandler: ...
    async def async_step_user(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_type(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_manual_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_secure_manual(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_secure_knxkeys(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_routing(self, user_input: Union[dict, None] = ...) -> FlowResult: ...

class KNXOptionsFlowHandler(OptionsFlow):
    general_settings: dict
    current_config: dict
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_tunnel(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

def get_knx_tunneling_type(config_entry_data: dict) -> str: ...
async def scan_for_gateways(stop_on_found: int = ...) -> list[GatewayDescriptor]: ...
