from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from .. import InvalidAuthError as InvalidAuthError
from ..models import Credentials as Credentials, RefreshToken as RefreshToken, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any, Union

IPAddress = Union[IPv4Address, IPv6Address]
IPNetwork = Union[IPv4Network, IPv6Network]
CONF_TRUSTED_NETWORKS: str
CONF_TRUSTED_USERS: str
CONF_GROUP: str
CONF_ALLOW_BYPASS_LOGIN: str
CONFIG_SCHEMA: Incomplete

class InvalidUserError(HomeAssistantError): ...

class TrustedNetworksAuthProvider(AuthProvider):
    DEFAULT_TITLE: str
    @property
    def trusted_networks(self) -> list[IPNetwork]: ...
    @property
    def trusted_users(self) -> dict[IPNetwork, Any]: ...
    @property
    def trusted_proxies(self) -> list[IPNetwork]: ...
    @property
    def support_mfa(self) -> bool: ...
    async def async_login_flow(self, context: Union[dict[str, Any], None]) -> LoginFlow: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...
    def async_validate_access(self, ip_addr: IPAddress) -> None: ...
    def async_validate_refresh_token(self, refresh_token: RefreshToken, remote_ip: Union[str, None] = ...) -> None: ...

class TrustedNetworksLoginFlow(LoginFlow):
    _available_users: Incomplete
    _ip_address: Incomplete
    _allow_bypass_login: Incomplete
    def __init__(self, auth_provider: TrustedNetworksAuthProvider, ip_addr: IPAddress, available_users: dict[str, Union[str, None]], allow_bypass_login: bool) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
