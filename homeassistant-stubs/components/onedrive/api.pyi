from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from onedrive_personal_sdk import TokenProvider

class OneDriveConfigFlowAccessTokenProvider(TokenProvider):
    _token: Incomplete
    def __init__(self, token: str) -> None: ...
    def async_get_access_token(self) -> str: ...

class OneDriveConfigEntryAccessTokenProvider(TokenProvider):
    _oauth_session: Incomplete
    def __init__(self, oauth_session: config_entry_oauth2_flow.OAuth2Session) -> None: ...
    def async_get_access_token(self) -> str: ...
