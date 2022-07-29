from _typeshed import Incomplete
from homeassistant.components.repairs import async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.components.repairs.models import IssueSeverity as IssueSeverity
from homeassistant.const import __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.yaml import parse_yaml as parse_yaml

DOMAIN: str
UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class IntegrationAlert:
    integration: str
    filename: str
    date_updated: Union[str, None]
    @property
    def issue_id(self) -> str: ...
    def __init__(self, integration, filename, date_updated) -> None: ...

class AlertUpdateCoordinator(DataUpdateCoordinator[dict[str, IntegrationAlert]]):
    ha_version: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[str, IntegrationAlert]: ...
