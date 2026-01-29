from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nrgkick_api import NRGkickAPI as NRGkickAPI
from typing import Any

_LOGGER: Incomplete
type NRGkickConfigEntry = ConfigEntry[NRGkickDataUpdateCoordinator]

@dataclass(slots=True)
class NRGkickData:
    info: dict[str, Any]
    control: dict[str, Any]
    values: dict[str, Any]

class NRGkickDataUpdateCoordinator(DataUpdateCoordinator[NRGkickData]):
    config_entry: NRGkickConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: NRGkickAPI, entry: NRGkickConfigEntry) -> None: ...
    async def _async_update_data(self) -> NRGkickData: ...
