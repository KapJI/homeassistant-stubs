from _typeshed import Incomplete
from esphome_dashboard_api import ConfiguredDevice
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
MIN_VERSION_SUPPORTS_UPDATE: Incomplete
REFRESH_INTERVAL: Incomplete

class ESPHomeDashboardCoordinator(DataUpdateCoordinator[dict[str, ConfiguredDevice]]):
    addon_slug: Incomplete
    url: Incomplete
    api: Incomplete
    supports_update: bool | None
    def __init__(self, hass: HomeAssistant, addon_slug: str, url: str) -> None: ...
    async def _async_update_data(self) -> dict[str, ConfiguredDevice]: ...
