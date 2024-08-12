from . import YALEXSBLEConfigEntry as YALEXSBLEConfigEntry
from .entity import YALEXSBLEEntity as YALEXSBLEEntity
from .models import YaleXSBLEData as YaleXSBLEData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

@dataclass(frozen=True, kw_only=True)
class YaleXSBLESensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[LockState, LockInfo, ConnectionInfo], int | float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SENSORS: tuple[YaleXSBLESensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YALEXSBLEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleXSBLESensor(YALEXSBLEEntity, SensorEntity):
    entity_description: YaleXSBLESensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: YaleXSBLESensorEntityDescription, data: YaleXSBLEData) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_state(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
