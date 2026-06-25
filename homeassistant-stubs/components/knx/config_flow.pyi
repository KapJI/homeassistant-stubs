from .const import CONF_KNX_AUTOMATIC as CONF_KNX_AUTOMATIC, CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_DEFAULT_RATE_LIMIT as CONF_KNX_DEFAULT_RATE_LIMIT, CONF_KNX_DEFAULT_STATE_UPDATER as CONF_KNX_DEFAULT_STATE_UPDATER, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_LOCAL_IP as CONF_KNX_LOCAL_IP, CONF_KNX_MCAST_GRP as CONF_KNX_MCAST_GRP, CONF_KNX_MCAST_PORT as CONF_KNX_MCAST_PORT, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_ROUTE_BACK as CONF_KNX_ROUTE_BACK, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_ROUTING_BACKBONE_KEY as CONF_KNX_ROUTING_BACKBONE_KEY, CONF_KNX_ROUTING_SECURE as CONF_KNX_ROUTING_SECURE, CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE as CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_ID as CONF_KNX_SECURE_USER_ID, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TELEGRAM_DB_LOAD_HOURS as CONF_KNX_TELEGRAM_DB_LOAD_HOURS, CONF_KNX_TELEGRAM_DB_RETENTION_DAYS as CONF_KNX_TELEGRAM_DB_RETENTION_DAYS, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, CONF_KNX_TUNNELING_TCP_SECURE as CONF_KNX_TUNNELING_TCP_SECURE, CONF_KNX_TUNNEL_ENDPOINT_IA as CONF_KNX_TUNNEL_ENDPOINT_IA, DEFAULT_ROUTING_IA as DEFAULT_ROUTING_IA, DOMAIN as DOMAIN, KNXConfigEntryData as KNXConfigEntryData, KNXConfigEntryOptions as KNXConfigEntryOptions, KNX_MODULE_KEY as KNX_MODULE_KEY, KNX_TELEGRAM_DB_RETENTION_DEFAULT as KNX_TELEGRAM_DB_RETENTION_DEFAULT, KNX_TELEGRAM_LOAD_HOURS_DEFAULT as KNX_TELEGRAM_LOAD_HOURS_DEFAULT
from .storage.keyring import DEFAULT_KNX_KEYRING_FILENAME as DEFAULT_KNX_KEYRING_FILENAME, save_uploaded_knxkeys_file as save_uploaded_knxkeys_file
from .validation import ia_validator as ia_validator, ip_v4_validator as ip_v4_validator
from _typeshed import Incomplete
from collections.abc import AsyncGenerator
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, VolDictType as VolDictType
from typing import Any, Final, override
from xknx import XKNX
from xknx.io.gateway_scanner import GatewayDescriptor as GatewayDescriptor, GatewayScanner
from xknx.secure.keyring import Keyring as Keyring, XMLInterface as XMLInterface

CONF_KNX_GATEWAY: Final[str]
CONF_MAX_RATE_LIMIT: Final[int]
DEFAULT_ENTRY_DATA: Incomplete
DEFAULT_ENTRY_OPTIONS: Incomplete
CONF_KEYRING_FILE: Final[str]
CONF_KNX_TELEGRAM_STORE_SECTION: Final[str]
CONF_KNX_TUNNELING_TYPE: Final[str]
CONF_KNX_TUNNELING_TYPE_LABELS: Final[Incomplete]
OPTION_MANUAL_TUNNEL: Final[str]
_IA_SELECTOR: Incomplete
_IP_SELECTOR: Incomplete
_PORT_SELECTOR: Incomplete

class KNXConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    initial_data: Incomplete
    new_entry_data: Incomplete
    new_title: str | None
    _keyring: Keyring | None
    _found_gateways: list[GatewayDescriptor]
    _found_tunnels: list[GatewayDescriptor]
    _selected_tunnel: GatewayDescriptor | None
    _tunnel_endpoints: list[XMLInterface]
    _gatewayscanner: GatewayScanner | None
    _async_scan_gen: AsyncGenerator[GatewayDescriptor] | None
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    @override
    def async_get_options_flow(config_entry: ConfigEntry) -> KNXOptionsFlow: ...
    @property
    def _xknx(self) -> XKNX: ...
    @property
    def connection_type(self) -> str: ...
    @property
    def tunnel_endpoint_ia(self) -> str | None: ...
    @callback
    def finish_flow(self) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_connection_type(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_tunnel(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_tcp_tunnel_endpoint(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_manual_tunnel(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_secure_tunnel_manual(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_secure_routing_manual(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_secure_knxkeys(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_knxkeys_tunnel_select(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_routing(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_secure_key_source_menu_tunnel(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_secure_key_source_menu_routing(self, user_input: dict | None = None) -> ConfigFlowResult: ...

class KNXOptionsFlow(OptionsFlowWithReload):
    initial_options: Incomplete
    new_entry_options: KNXConfigEntryOptions
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    @callback
    def finish_flow(self) -> ConfigFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_communication_settings(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
