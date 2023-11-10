from .const import ATTRIBUTION as ATTRIBUTION, ATTR_BYTES_RECEIVED as ATTR_BYTES_RECEIVED, ATTR_BYTES_SENT as ATTR_BYTES_SENT, ATTR_SERVER_COUNTRY as ATTR_SERVER_COUNTRY, ATTR_SERVER_ID as ATTR_SERVER_ID, ATTR_SERVER_NAME as ATTR_SERVER_NAME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, ICON as ICON
from .coordinator import SpeedTestDataCoordinator as SpeedTestDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfDataRate as UnitOfDataRate, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass
class SpeedtestSensorEntityDescription(SensorEntityDescription):
    value: Callable = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value) -> None: ...

SENSOR_TYPES: tuple[SpeedtestSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SpeedtestSensor(CoordinatorEntity[SpeedTestDataCoordinator], SensorEntity):
    entity_description: SpeedtestSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_icon = ICON
    _attr_unique_id: Incomplete
    _state: Incomplete
    _attrs: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SpeedTestDataCoordinator, description: SpeedtestSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
