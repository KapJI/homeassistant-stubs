from .const import DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HydrawiseSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[HydrawiseSensor], Any]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

def _get_zone_watering_time(sensor: HydrawiseSensor) -> int: ...
def _get_zone_next_cycle(sensor: HydrawiseSensor) -> datetime | None: ...
def _get_zone_daily_active_water_use(sensor: HydrawiseSensor) -> float: ...
def _get_zone_daily_active_water_time(sensor: HydrawiseSensor) -> float | None: ...
def _get_controller_daily_active_water_use(sensor: HydrawiseSensor) -> float | None: ...
def _get_controller_daily_inactive_water_use(sensor: HydrawiseSensor) -> float | None: ...
def _get_controller_daily_active_water_time(sensor: HydrawiseSensor) -> float: ...
def _get_controller_daily_total_water_use(sensor: HydrawiseSensor) -> float | None: ...

CONTROLLER_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_CONTROLLER_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_ZONE_SENSORS: tuple[SensorEntityDescription, ...]
ZONE_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_MEASUREMENT_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSensor(HydrawiseEntity, SensorEntity):
    entity_description: HydrawiseSensorEntityDescription
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    _attr_native_value: Incomplete
    def _update_attrs(self) -> None: ...
