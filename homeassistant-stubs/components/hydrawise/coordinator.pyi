from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, MAIN_SCAN_INTERVAL as MAIN_SCAN_INTERVAL, MODEL_ZONE as MODEL_ZONE, WATER_USE_SCAN_INTERVAL as WATER_USE_SCAN_INTERVAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import now as now
from pydrawise import HydrawiseBase as HydrawiseBase
from pydrawise.schema import Controller as Controller, ControllerWaterUseSummary as ControllerWaterUseSummary, Sensor as Sensor, User as User, Zone as Zone

type HydrawiseConfigEntry = ConfigEntry[HydrawiseUpdateCoordinators]
@dataclass
class HydrawiseData:
    user: User
    controllers: dict[int, Controller] = field(default_factory=dict)
    zones: dict[int, Zone] = field(default_factory=dict)
    zone_id_to_controller: dict[int, Controller] = field(default_factory=dict)
    sensors: dict[int, Sensor] = field(default_factory=dict)
    daily_water_summary: dict[int, ControllerWaterUseSummary] = field(default_factory=dict)

@dataclass
class HydrawiseUpdateCoordinators:
    main: HydrawiseMainDataUpdateCoordinator
    water_use: HydrawiseWaterUseDataUpdateCoordinator

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[HydrawiseData]):
    api: HydrawiseBase
    config_entry: HydrawiseConfigEntry

class HydrawiseMainDataUpdateCoordinator(HydrawiseDataUpdateCoordinator):
    api: Incomplete
    new_controllers_callbacks: list[Callable[[Iterable[Controller]], None]]
    new_zones_callbacks: list[Callable[[Iterable[tuple[Zone, Controller]]], None]]
    def __init__(self, hass: HomeAssistant, config_entry: HydrawiseConfigEntry, api: HydrawiseBase) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...
    @callback
    def _add_remove_zones(self) -> None: ...

class HydrawiseWaterUseDataUpdateCoordinator(HydrawiseDataUpdateCoordinator):
    _main_coordinator: HydrawiseMainDataUpdateCoordinator
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HydrawiseConfigEntry, api: HydrawiseBase, main_coordinator: HydrawiseMainDataUpdateCoordinator) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...
