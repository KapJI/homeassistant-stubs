from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from flow_it_api.client import FlowItVMCMachine as FlowItVMCMachine
from flow_it_api.models import MachineData as MachineData, MachineStatusResponse as MachineStatusResponse
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type FlowItConfigEntry = ConfigEntry[FlowItData]

@dataclass(kw_only=True, frozen=True)
class FlowItCoordinatorData:
    state: MachineStatusResponse

@dataclass(kw_only=True, frozen=True)
class FlowItData:
    vmc: FlowItVMCMachine
    coordinator: FlowItCoordinator

class FlowItCoordinator(DataUpdateCoordinator[FlowItCoordinatorData]):
    config_entry: FlowItConfigEntry
    vmc: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FlowItConfigEntry, vmc: FlowItVMCMachine) -> None: ...
    @override
    async def _async_update_data(self) -> FlowItCoordinatorData: ...
