from .const import INSTALLED_AUTH_DOMAIN as INSTALLED_AUTH_DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN, OOB_REDIRECT_URI as OOB_REDIRECT_URI, WEB_AUTH_DOMAIN as WEB_AUTH_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

class WebAuth(config_entry_oauth2_flow.LocalOAuth2Implementation):
    name: str
    def __init__(self, hass: HomeAssistant, client_id: str, client_secret: str, project_id: str) -> None: ...

class InstalledAppAuth(config_entry_oauth2_flow.LocalOAuth2Implementation):
    name: str
    def __init__(self, hass: HomeAssistant, client_id: str, client_secret: str, project_id: str) -> None: ...
    @property
    def redirect_uri(self) -> str: ...
