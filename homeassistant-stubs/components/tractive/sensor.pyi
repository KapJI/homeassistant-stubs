from . import Trackables as Trackables, TractiveClient as TractiveClient
from .const import ATTR_ACTIVITY_LABEL as ATTR_ACTIVITY_LABEL, ATTR_CALORIES as ATTR_CALORIES, ATTR_DAILY_GOAL as ATTR_DAILY_GOAL, ATTR_MINUTES_ACTIVE as ATTR_MINUTES_ACTIVE, ATTR_MINUTES_DAY_SLEEP as ATTR_MINUTES_DAY_SLEEP, ATTR_MINUTES_NIGHT_SLEEP as ATTR_MINUTES_NIGHT_SLEEP, ATTR_MINUTES_REST as ATTR_MINUTES_REST, ATTR_SLEEP_LABEL as ATTR_SLEEP_LABEL, ATTR_TRACKER_STATE as ATTR_TRACKER_STATE, CLIENT as CLIENT, DOMAIN as DOMAIN, TRACKABLES as TRACKABLES, TRACKER_ACTIVITY_STATUS_UPDATED as TRACKER_ACTIVITY_STATUS_UPDATED, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED, TRACKER_WELLNESS_STATUS_UPDATED as TRACKER_WELLNESS_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

class TractiveRequiredKeysMixin:
    signal_prefix: str
    def __init__(self, signal_prefix) -> None: ...

class TractiveSensorEntityDescription(SensorEntityDescription, TractiveRequiredKeysMixin):
    hardware_sensor: bool
    value_fn: Callable[[StateType], StateType]
    def __init__(self, signal_prefix, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, hardware_sensor, value_fn) -> None: ...

class TractiveSensor(TractiveEntity, SensorEntity):
    entity_description: TractiveSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_available: bool
    def __init__(self, client: TractiveClient, item: Trackables, description: TractiveSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def handle_status_update(self, event: dict[str, Any]) -> None: ...

SENSOR_TYPES: tuple[TractiveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
