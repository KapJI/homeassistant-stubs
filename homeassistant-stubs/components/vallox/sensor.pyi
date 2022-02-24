from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, MODE_ON as MODE_ON, VALLOX_CELL_STATE_TO_STR as VALLOX_CELL_STATE_TO_STR, VALLOX_PROFILE_TO_STR_REPORTABLE as VALLOX_PROFILE_TO_STR_REPORTABLE
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import dt as dt
from typing import Any

class ValloxSensor(CoordinatorEntity, SensorEntity):
    entity_description: ValloxSensorEntityDescription
    coordinator: ValloxDataUpdateCoordinator
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxProfileSensor(ValloxSensor):
    @property
    def native_value(self) -> StateType: ...

class ValloxFanSpeedSensor(ValloxSensor):
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxFilterRemainingSensor(ValloxSensor):
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxCellStateSensor(ValloxSensor):
    @property
    def native_value(self) -> StateType: ...

class ValloxSensorEntityDescription(SensorEntityDescription):
    metric_key: Union[str, None]
    sensor_type: type[ValloxSensor]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, metric_key, sensor_type) -> None: ...

SENSORS: tuple[ValloxSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
