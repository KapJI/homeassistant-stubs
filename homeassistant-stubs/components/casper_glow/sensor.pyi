from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from .entity import CasperGlowEntity as CasperGlowEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from pycasperglow import GlowState as GlowState

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CasperGlowBatterySensor(CasperGlowEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_state_update(self, state: GlowState) -> None: ...

class CasperGlowDimmingEndTimeSensor(CasperGlowEntity, SensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_unique_id: Incomplete
    _is_paused: bool
    _projected_end_time: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    @staticmethod
    def _calculate_end_time(remaining_ms: int) -> datetime: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def _reset_projected_end_time(self) -> None: ...
    @callback
    def _update_from_state(self, state: GlowState) -> None: ...
    @callback
    def _async_handle_state_update(self, state: GlowState) -> None: ...
