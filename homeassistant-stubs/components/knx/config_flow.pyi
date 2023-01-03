import abc
from .const import CONF_KNX_AUTOMATIC as CONF_KNX_AUTOMATIC, CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_DEFAULT_RATE_LIMIT as CONF_KNX_DEFAULT_RATE_LIMIT, CONF_KNX_DEFAULT_STATE_UPDATER as CONF_KNX_DEFAULT_STATE_UPDATER, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_KNXKEY_FILENAME as CONF_KNX_KNXKEY_FILENAME, CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_LOCAL_IP as CONF_KNX_LOCAL_IP, CONF_KNX_MCAST_GRP as CONF_KNX_MCAST_GRP, CONF_KNX_MCAST_PORT as CONF_KNX_MCAST_PORT, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_ROUTE_BACK as CONF_KNX_ROUTE_BACK, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_ROUTING_BACKBONE_KEY as CONF_KNX_ROUTING_BACKBONE_KEY, CONF_KNX_ROUTING_SECURE as CONF_KNX_ROUTING_SECURE, CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE as CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_ID as CONF_KNX_SECURE_USER_ID, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, CONF_KNX_TUNNELING_TCP_SECURE as CONF_KNX_TUNNELING_TCP_SECURE, CONST_KNX_STORAGE_KEY as CONST_KNX_STORAGE_KEY, DEFAULT_ROUTING_IA as DEFAULT_ROUTING_IA, DOMAIN as DOMAIN, KNXConfigEntryData as KNXConfigEntryData
from .schema import ia_validator as ia_validator, ip_v4_validator as ip_v4_validator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowHandler as FlowHandler, FlowResult as FlowResult
from homeassistant.helpers import selector as selector
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from typing import Any, Final
from xknx.io.gateway_scanner import GatewayDescriptor as GatewayDescriptor
from xknx.secure.keyring import XMLInterface as XMLInterface

CONF_KNX_GATEWAY: Final[str]
CONF_MAX_RATE_LIMIT: Final[int]
DEFAULT_ENTRY_DATA: Incomplete
CONF_KNX_TUNNELING_TYPE: Final[str]
CONF_KNX_TUNNELING_TYPE_LABELS: Final[Incomplete]
OPTION_MANUAL_TUNNEL: Final[str]
_IA_SELECTOR: Incomplete
_IP_SELECTOR: Incomplete
_PORT_SELECTOR: Incomplete

class KNXCommonFlow(ABC, FlowHandler, metaclass=abc.ABCMeta):
    initial_data: Incomplete
    new_entry_data: Incomplete
    _found_gateways: Incomplete
    _found_tunnels: Incomplete
    _selected_tunnel: Incomplete
    _tunnel_endpoints: Incomplete
    _gatewayscanner: Incomplete
    _async_scan_gen: Incomplete
    def __init__(self, initial_data: KNXConfigEntryData) -> None: ...
    @abstractmethod
    def finish_flow(self, title: str) -> FlowResult: ...
    async def async_step_connection_type(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_manual_tunnel(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_secure_tunnel_manual(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_secure_routing_manual(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_secure_knxkeys(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_knxkeys_tunnel_select(self, user_input: Union[dict, None] = ...) -> FlowResult: ...
    async def async_step_routing(self, user_input: Union[dict, None] = ...) -> FlowResult: ...

class KNXConfigFlow(KNXCommonFlow, ConfigFlow):
    VERSION: int
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> KNXOptionsFlow: ...
    def finish_flow(self, title: str) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict, None] = ...) -> FlowResult: ...

class KNXOptionsFlow(KNXCommonFlow, OptionsFlow):
    general_settings: dict
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    def finish_flow(self, title: Union[str, None]) -> FlowResult: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    new_entry_data: Incomplete
    async def async_step_communication_settings(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
