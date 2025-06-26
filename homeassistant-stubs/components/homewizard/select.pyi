from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator, HomeWizardConfigEntry as HomeWizardConfigEntry
from .entity import HomeWizardEntity as HomeWizardEntity
from .helpers import homewizard_exception_handler as homewizard_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homewizard_energy import HomeWizardEnergy as HomeWizardEnergy
from homewizard_energy.models import CombinedModels as DeviceResponseEntry
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HomeWizardSelectEntityDescription(SelectEntityDescription):
    available_fn: Callable[[DeviceResponseEntry], bool]
    create_fn: Callable[[DeviceResponseEntry], bool]
    current_fn: Callable[[DeviceResponseEntry], str | None]
    set_fn: Callable[[HomeWizardEnergy, str], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeWizardSelectEntity(HomeWizardEntity, SelectEntity):
    entity_description: HomeWizardSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @homewizard_exception_handler
    async def async_select_option(self, option: str) -> None: ...
