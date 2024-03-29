from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from amberelectric.api import amber_api as amber_api
from amberelectric.model.actual_interval import ActualInterval as ActualInterval
from amberelectric.model.current_interval import CurrentInterval
from amberelectric.model.forecast_interval import ForecastInterval
from amberelectric.model.interval import Descriptor as Descriptor
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

def is_current(interval: ActualInterval | CurrentInterval | ForecastInterval) -> bool: ...
def is_forecast(interval: ActualInterval | CurrentInterval | ForecastInterval) -> bool: ...
def is_general(interval: ActualInterval | CurrentInterval | ForecastInterval) -> bool: ...
def is_controlled_load(interval: ActualInterval | CurrentInterval | ForecastInterval) -> bool: ...
def is_feed_in(interval: ActualInterval | CurrentInterval | ForecastInterval) -> bool: ...
def normalize_descriptor(descriptor: Descriptor) -> str | None: ...

class AmberUpdateCoordinator(DataUpdateCoordinator):
    _api: Incomplete
    site_id: Incomplete
    def __init__(self, hass: HomeAssistant, api: amber_api.AmberApi, site_id: str) -> None: ...
    def update_price_data(self) -> dict[str, dict[str, Any]]: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
