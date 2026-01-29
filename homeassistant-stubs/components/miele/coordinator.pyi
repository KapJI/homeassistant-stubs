from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pymiele import MieleAPI as MieleAPI, MieleAction, MieleDevice, MieleFillingLevel as MieleFillingLevel

_LOGGER: Incomplete

@dataclass
class MieleRuntimeData:
    api: MieleAPI
    coordinator: MieleDataUpdateCoordinator
    aux_coordinator: MieleAuxDataUpdateCoordinator
type MieleConfigEntry = ConfigEntry[MieleRuntimeData]

@dataclass
class MieleCoordinatorData:
    devices: dict[str, MieleDevice]
    actions: dict[str, MieleAction]

@dataclass
class MieleAuxCoordinatorData:
    filling_levels: dict[str, MieleFillingLevel]

class MieleDataUpdateCoordinator(DataUpdateCoordinator[MieleCoordinatorData]):
    config_entry: MieleConfigEntry
    new_device_callbacks: list[Callable[[dict[str, MieleDevice]], None]]
    known_devices: set[str]
    devices: dict[str, MieleDevice]
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: MieleConfigEntry, api: MieleAPI) -> None: ...
    async def _async_update_data(self) -> MieleCoordinatorData: ...
    def async_add_devices(self, added_devices: set[str]) -> tuple[set[str], set[str]]: ...
    async def callback_update_data(self, devices_json: dict[str, dict]) -> None: ...
    async def callback_update_actions(self, actions_json: dict[str, dict]) -> None: ...

class MieleAuxDataUpdateCoordinator(DataUpdateCoordinator[MieleAuxCoordinatorData]):
    config_entry: MieleConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: MieleConfigEntry, api: MieleAPI) -> None: ...
    async def _async_update_data(self) -> MieleAuxCoordinatorData: ...
