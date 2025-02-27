from .const import AIOAIRZONE_DEVICE_TIMEOUT_SEC as AIOAIRZONE_DEVICE_TIMEOUT_SEC, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioairzone.localapi import AirzoneLocalApi as AirzoneLocalApi
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type AirzoneConfigEntry = ConfigEntry[AirzoneUpdateCoordinator]

class AirzoneUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: AirzoneConfigEntry
    airzone: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirzoneConfigEntry, airzone: AirzoneLocalApi) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
