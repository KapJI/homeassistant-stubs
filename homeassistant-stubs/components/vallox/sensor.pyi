from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator, ValloxEntity as ValloxEntity
from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, MODE_ON as MODE_ON, VALLOX_CELL_STATE_TO_STR as VALLOX_CELL_STATE_TO_STR, VALLOX_PROFILE_TO_STR_REPORTABLE as VALLOX_PROFILE_TO_STR_REPORTABLE
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, FREQUENCY_HERTZ as FREQUENCY_HERTZ, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import dt as dt

class ValloxSensorEntity(ValloxEntity, SensorEntity):
    entity_description: ValloxSensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxProfileSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType: ...

class ValloxFanSpeedSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxFilterRemainingSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> Union[StateType, datetime]: ...

class ValloxCellStateSensor(ValloxSensorEntity):
    @property
    def native_value(self) -> StateType: ...

class ValloxSensorEntityDescription(SensorEntityDescription):
    metric_key: Union[str, None]
    entity_type: type[ValloxSensorEntity]
    round_ndigits: Union[int, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, metric_key, entity_type, round_ndigits) -> None: ...

SENSOR_ENTITIES: tuple[ValloxSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
