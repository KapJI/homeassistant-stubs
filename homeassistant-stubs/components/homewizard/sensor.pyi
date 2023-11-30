from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homewizard_energy.models import Data as Data
from typing import Final

PARALLEL_UPDATES: int

@dataclass(kw_only=True)
class HomeWizardSensorEntityDescription(SensorEntityDescription):
    enabled_fn: Callable[[Data], bool] = ...
    has_fn: Callable[[Data], bool]
    value_fn: Callable[[Data], StateType]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, *, enabled_fn, has_fn, value_fn) -> None: ...

SENSORS: Final[tuple[HomeWizardSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeWizardSensorEntity(HomeWizardEntity, SensorEntity):
    entity_description: HomeWizardSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
