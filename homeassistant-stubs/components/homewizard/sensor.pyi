from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator, HomeWizardConfigEntry as HomeWizardConfigEntry
from .entity import HomeWizardEntity as HomeWizardEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from homewizard_energy.models import CombinedModels as CombinedModels, ExternalDevice
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HomeWizardSensorEntityDescription(SensorEntityDescription):
    enabled_fn: Callable[[CombinedModels], bool] = ...
    has_fn: Callable[[CombinedModels], bool]
    value_fn: Callable[[CombinedModels], StateType | datetime]

@dataclass(frozen=True, kw_only=True)
class HomeWizardExternalSensorEntityDescription(SensorEntityDescription):
    suggested_device_class: SensorDeviceClass
    device_name: str

def to_percentage(value: float | None) -> float | None: ...
def time_to_datetime(value: int | None) -> datetime | None: ...

SENSORS: Final[tuple[HomeWizardSensorEntityDescription, ...]]
EXTERNAL_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeWizardSensorEntity(HomeWizardEntity, SensorEntity):
    entity_description: HomeWizardSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime | None: ...
    @property
    def available(self) -> bool: ...

class HomeWizardExternalSensorEntity(HomeWizardEntity, SensorEntity):
    entity_description: Incomplete
    _device_id: Incomplete
    _suggested_device_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardExternalSensorEntityDescription, device_unique_id: str) -> None: ...
    @property
    def native_value(self) -> float | int | str | None: ...
    @property
    def device(self) -> ExternalDevice | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
