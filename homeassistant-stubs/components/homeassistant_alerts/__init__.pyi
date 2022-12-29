from _typeshed import Incomplete
from homeassistant.components.hassio import get_supervisor_info as get_supervisor_info, is_hassio as is_hassio
from homeassistant.const import __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.start import async_at_start as async_at_start
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

DOMAIN: str
UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class IntegrationAlert:
    alert_id: str
    integration: str
    filename: str
    date_updated: Union[str, None]
    @property
    def issue_id(self) -> str: ...
    def __init__(self, alert_id, integration, filename, date_updated) -> None: ...

class AlertUpdateCoordinator(DataUpdateCoordinator[dict[str, IntegrationAlert]]):
    ha_version: Incomplete
    supervisor: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[str, IntegrationAlert]: ...
