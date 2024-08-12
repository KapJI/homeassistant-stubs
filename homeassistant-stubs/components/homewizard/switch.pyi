from . import HomeWizardConfigEntry as HomeWizardConfigEntry
from .const import DeviceResponseEntry as DeviceResponseEntry
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from .helpers import homewizard_exception_handler as homewizard_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homewizard_energy import HomeWizardEnergy as HomeWizardEnergy
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HomeWizardSwitchEntityDescription(SwitchEntityDescription):
    available_fn: Callable[[DeviceResponseEntry], bool]
    create_fn: Callable[[HWEnergyDeviceUpdateCoordinator], bool]
    is_on_fn: Callable[[DeviceResponseEntry], bool | None]
    set_fn: Callable[[HomeWizardEnergy, bool], Awaitable[Any]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., available_fn, create_fn, is_on_fn, set_fn) -> None: ...

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeWizardSwitchEntity(HomeWizardEntity, SwitchEntity):
    entity_description: HomeWizardSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardSwitchEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
