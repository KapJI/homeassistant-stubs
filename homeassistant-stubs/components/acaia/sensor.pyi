from .coordinator import AcaiaConfigEntry as AcaiaConfigEntry
from .entity import AcaiaEntity as AcaiaEntity
from _typeshed import Incomplete
from aioacaia.acaiascale import AcaiaDeviceState as AcaiaDeviceState, AcaiaScale as AcaiaScale
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfMass as UnitOfMass, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class AcaiaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AcaiaScale], int | float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

@dataclass(kw_only=True, frozen=True)
class AcaiaDynamicUnitSensorEntityDescription(AcaiaSensorEntityDescription):
    unit_fn: Callable[[AcaiaDeviceState], str] | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn, unit_fn=...) -> None: ...

SENSORS: tuple[AcaiaSensorEntityDescription, ...]
RESTORE_SENSORS: tuple[AcaiaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AcaiaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AcaiaSensor(AcaiaEntity, SensorEntity):
    entity_description: AcaiaDynamicUnitSensorEntityDescription
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> int | float | None: ...

class AcaiaRestoreSensor(AcaiaEntity, RestoreSensor):
    entity_description: AcaiaSensorEntityDescription
    _restored_data: SensorExtraStoredData | None
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
