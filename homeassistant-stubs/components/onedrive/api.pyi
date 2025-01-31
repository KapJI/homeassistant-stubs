from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from kiota_abstractions.authentication import AccessTokenProvider, AllowedHostsValidator
from typing import Any

class OneDriveAccessTokenProvider(AccessTokenProvider):
    _allowed_hosts_validator: Incomplete
    def __init__(self) -> None: ...
    def get_allowed_hosts_validator(self) -> AllowedHostsValidator: ...

class OneDriveConfigFlowAccessTokenProvider(OneDriveAccessTokenProvider):
    _token: Incomplete
    def __init__(self, token: str) -> None: ...
    async def get_authorization_token(self, uri: str, additional_authentication_context: dict[str, Any] = {}) -> str: ...

class OneDriveConfigEntryAccessTokenProvider(OneDriveAccessTokenProvider):
    _oauth_session: Incomplete
    def __init__(self, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    async def get_authorization_token(self, uri: str, additional_authentication_context: dict[str, Any] = {}) -> str: ...
