from . import WattsVisionRuntimeData as WattsVisionRuntimeData
from .const import DISCOVERY_INTERVAL_MINUTES as DISCOVERY_INTERVAL_MINUTES, DOMAIN as DOMAIN, FAST_POLLING_INTERVAL_SECONDS as FAST_POLLING_INTERVAL_SECONDS, UPDATE_INTERVAL_SECONDS as UPDATE_INTERVAL_SECONDS
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from visionpluspython.client import WattsVisionClient as WattsVisionClient
from visionpluspython.models import Device, ThermostatDevice

type WattsVisionConfigEntry = ConfigEntry[WattsVisionRuntimeData]
_LOGGER: Incomplete

@dataclass
class WattsVisionThermostatData:
    thermostat: ThermostatDevice

class WattsVisionHubCoordinator(DataUpdateCoordinator[dict[str, Device]]):
    client: Incomplete
    _last_discovery: datetime | None
    previous_devices: set[str]
    def __init__(self, hass: HomeAssistant, client: WattsVisionClient, config_entry: WattsVisionConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, Device]: ...
    async def _remove_stale_devices(self, stale_device_ids: set[str]) -> None: ...
    @property
    def device_ids(self) -> list[str]: ...

class WattsVisionThermostatCoordinator(DataUpdateCoordinator[WattsVisionThermostatData]):
    client: Incomplete
    device_id: Incomplete
    hub_coordinator: Incomplete
    _fast_polling_until: datetime | None
    unsubscribe_hub_listener: Incomplete
    def __init__(self, hass: HomeAssistant, client: WattsVisionClient, config_entry: WattsVisionConfigEntry, hub_coordinator: WattsVisionHubCoordinator, device_id: str) -> None: ...
    def _handle_hub_update(self) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> WattsVisionThermostatData: ...
    def trigger_fast_polling(self, duration: int = 60) -> None: ...
