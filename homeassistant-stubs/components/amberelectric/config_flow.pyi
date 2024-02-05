from .const import CONF_SITE_ID as CONF_SITE_ID, CONF_SITE_NAME as CONF_SITE_NAME, CONF_SITE_NMI as CONF_SITE_NMI, DOMAIN as DOMAIN
from _typeshed import Incomplete
from amberelectric.model.site import Site as Site
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult

API_URL: str

class AmberElectricConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: Incomplete
    _sites: Incomplete
    _api_token: Incomplete
    def __init__(self) -> None: ...
    def _fetch_sites(self, token: str) -> list[Site] | None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
    async def async_step_site(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
