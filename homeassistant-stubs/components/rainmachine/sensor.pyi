from . import RainMachineEntity as RainMachineEntity
from .const import DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN, RUN_STATE_MAP as RUN_STATE_MAP, RunStates as RunStates
from .model import RainMachineDescriptionMixinApiCategory as RainMachineDescriptionMixinApiCategory, RainMachineDescriptionMixinUid as RainMachineDescriptionMixinUid
from .util import key_exists as key_exists
from _typeshed import Incomplete
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import utcnow as utcnow
from regenmaschine.controller import Controller as Controller
from typing import Any

DEFAULT_ZONE_COMPLETION_TIME_WOBBLE_TOLERANCE: Incomplete
TYPE_FLOW_SENSOR_CLICK_M3: str
TYPE_FLOW_SENSOR_CONSUMED_LITERS: str
TYPE_FLOW_SENSOR_START_INDEX: str
TYPE_FLOW_SENSOR_WATERING_CLICKS: str
TYPE_FREEZE_TEMP: str
TYPE_PROGRAM_RUN_COMPLETION_TIME: str
TYPE_ZONE_RUN_COMPLETION_TIME: str

class RainMachineSensorDescriptionApiCategory(SensorEntityDescription, RainMachineDescriptionMixinApiCategory):
    def __init__(self, api_category, data_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

class RainMachineSensorDescriptionUid(SensorEntityDescription, RainMachineDescriptionMixinUid):
    def __init__(self, uid, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TimeRemainingSensor(RainMachineEntity, RestoreSensor):
    entity_description: RainMachineSensorDescriptionUid
    _current_run_state: Incomplete
    _previous_run_state: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, controller: Controller, description: EntityDescription) -> None: ...
    @property
    def activity_data(self) -> dict[str, Any]: ...
    @property
    def status_key(self) -> str: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def calculate_seconds_remaining(self) -> int: ...
    def update_from_latest_data(self) -> None: ...

class ProgramTimeRemainingSensor(TimeRemainingSensor):
    _zone_coordinator: Incomplete
    def __init__(self, entry: ConfigEntry, program_coordinator: DataUpdateCoordinator, zone_coordinator: DataUpdateCoordinator, controller: Controller, description: EntityDescription) -> None: ...
    @property
    def status_key(self) -> str: ...
    def calculate_seconds_remaining(self) -> int: ...

class ProvisionSettingsSensor(RainMachineEntity, SensorEntity):
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class UniversalRestrictionsSensor(RainMachineEntity, SensorEntity):
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class ZoneTimeRemainingSensor(TimeRemainingSensor):
    def calculate_seconds_remaining(self) -> int: ...
