from . import Trackables as Trackables
from .const import ATTR_DAILY_GOAL as ATTR_DAILY_GOAL, ATTR_MINUTES_ACTIVE as ATTR_MINUTES_ACTIVE, ATTR_TRACKER_STATE as ATTR_TRACKER_STATE, CLIENT as CLIENT, DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKABLES as TRACKABLES, TRACKER_ACTIVITY_STATUS_UPDATED as TRACKER_ACTIVITY_STATUS_UPDATED, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class TractiveRequiredKeysMixin:
    entity_class: type[TractiveSensor]
    def __init__(self, entity_class) -> None: ...

class TractiveSensorEntityDescription(SensorEntityDescription, TractiveRequiredKeysMixin):
    def __init__(self, entity_class, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

class TractiveSensor(TractiveEntity, SensorEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, user_id: str, item: Trackables, description: TractiveSensorEntityDescription) -> None: ...
    _attr_available: bool
    def handle_server_unavailable(self) -> None: ...

class TractiveHardwareSensor(TractiveSensor):
    _attr_native_value: Incomplete
    _attr_available: bool
    def handle_hardware_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class TractiveActivitySensor(TractiveSensor):
    _attr_native_value: Incomplete
    _attr_available: bool
    def handle_activity_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

SENSOR_TYPES: tuple[TractiveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
