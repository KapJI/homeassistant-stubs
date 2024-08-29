from . import HomeWizardConfigEntry as HomeWizardConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homewizard_energy.models import Data as Data, ExternalDevice
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HomeWizardSensorEntityDescription(SensorEntityDescription):
    enabled_fn: Callable[[Data], bool] = ...
    has_fn: Callable[[Data], bool]
    value_fn: Callable[[Data], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., enabled_fn=..., has_fn, value_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class HomeWizardExternalSensorEntityDescription(SensorEntityDescription):
    suggested_device_class: SensorDeviceClass
    device_name: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., suggested_device_class, device_name) -> None: ...

def to_percentage(value: float | None) -> float | None: ...

SENSORS: Final[tuple[HomeWizardSensorEntityDescription, ...]]
EXTERNAL_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeWizardSensorEntity(HomeWizardEntity, SensorEntity):
    entity_description: HomeWizardSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, description: HomeWizardSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
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
