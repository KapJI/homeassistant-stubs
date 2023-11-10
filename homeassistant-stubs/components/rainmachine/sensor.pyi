from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity
from .const import DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey as RainMachineEntityDescriptionMixinDataKey, RainMachineEntityDescriptionMixinUid as RainMachineEntityDescriptionMixinUid
from .util import EntityDomainReplacementStrategy as EntityDomainReplacementStrategy, RUN_STATE_MAP as RUN_STATE_MAP, RunStates as RunStates, async_finish_entity_domain_replacements as async_finish_entity_domain_replacements, key_exists as key_exists
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp, utcnow as utcnow
from typing import Any

DEFAULT_ZONE_COMPLETION_TIME_WOBBLE_TOLERANCE: Incomplete
TYPE_FLOW_SENSOR_CLICK_M3: str
TYPE_FLOW_SENSOR_CONSUMED_LITERS: str
TYPE_FLOW_SENSOR_LEAK_CLICKS: str
TYPE_FLOW_SENSOR_LEAK_VOLUME: str
TYPE_FLOW_SENSOR_START_INDEX: str
TYPE_FLOW_SENSOR_WATERING_CLICKS: str
TYPE_LAST_LEAK_DETECTED: str
TYPE_PROGRAM_RUN_COMPLETION_TIME: str
TYPE_RAIN_SENSOR_RAIN_START: str
TYPE_ZONE_RUN_COMPLETION_TIME: str

@dataclass
class RainMachineSensorDataDescription(SensorEntityDescription, RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey):
    def __init__(self, data_key, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

@dataclass
class RainMachineSensorCompletionTimerDescription(SensorEntityDescription, RainMachineEntityDescription, RainMachineEntityDescriptionMixinUid):
    def __init__(self, uid, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TimeRemainingSensor(RainMachineEntity, RestoreSensor):
    entity_description: RainMachineSensorCompletionTimerDescription
    _current_run_state: Incomplete
    _previous_run_state: Incomplete
    def __init__(self, entry: ConfigEntry, data: RainMachineData, description: RainMachineSensorCompletionTimerDescription) -> None: ...
    @property
    def activity_data(self) -> dict[str, Any]: ...
    @property
    def status_key(self) -> str: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def calculate_seconds_remaining(self) -> int: ...
    def update_from_latest_data(self) -> None: ...

class ProgramTimeRemainingSensor(TimeRemainingSensor):
    @property
    def status_key(self) -> str: ...
    def calculate_seconds_remaining(self) -> int: ...

class ProvisionSettingsSensor(RainMachineEntity, SensorEntity):
    entity_description: RainMachineSensorDataDescription
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class ZoneTimeRemainingSensor(TimeRemainingSensor):
    def calculate_seconds_remaining(self) -> int: ...
