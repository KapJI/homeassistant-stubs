from . import AnalyticsInsightsConfigEntry as AnalyticsInsightsConfigEntry
from .const import CONF_TRACKED_CUSTOM_INTEGRATIONS as CONF_TRACKED_CUSTOM_INTEGRATIONS, CONF_TRACKED_INTEGRATIONS as CONF_TRACKED_INTEGRATIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_homeassistant_analytics import CustomIntegration as CustomIntegration, HomeassistantAnalyticsClient as HomeassistantAnalyticsClient

@dataclass(frozen=True)
class AnalyticsData:
    core_integrations: dict[str, int]
    custom_integrations: dict[str, int]
    def __init__(self, core_integrations, custom_integrations) -> None: ...

class HomeassistantAnalyticsDataUpdateCoordinator(DataUpdateCoordinator[AnalyticsData]):
    config_entry: AnalyticsInsightsConfigEntry
    _client: Incomplete
    _tracked_integrations: Incomplete
    _tracked_custom_integrations: Incomplete
    def __init__(self, hass: HomeAssistant, client: HomeassistantAnalyticsClient) -> None: ...
    async def _async_update_data(self) -> AnalyticsData: ...

def get_custom_integration_value(data: dict[str, CustomIntegration], domain: str) -> int: ...
