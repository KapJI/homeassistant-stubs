import pybotvac
from homeassistant import config_entries as config_entries, core as core
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class ConfigEntryAuth(pybotvac.OAuthSession):
    hass: Any
    session: Any
    def __init__(self, hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry, implementation: config_entry_oauth2_flow.AbstractOAuth2Implementation) -> None: ...
    def refresh_tokens(self) -> str: ...

class NeatoImplementation(config_entry_oauth2_flow.LocalOAuth2Implementation):
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_generate_authorize_url(self, flow_id: str) -> str: ...
