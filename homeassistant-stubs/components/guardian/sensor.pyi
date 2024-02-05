from . import GuardianData as GuardianData, PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_VALVE_STATUS as API_VALVE_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

SENSOR_KIND_AVG_CURRENT: str
SENSOR_KIND_BATTERY: str
SENSOR_KIND_INST_CURRENT: str
SENSOR_KIND_INST_CURRENT_DDT: str
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_TRAVEL_COUNT: str
SENSOR_KIND_UPTIME: str

@dataclass(frozen=True, kw_only=True)
class PairedSensorDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValveControllerSensorDescription(SensorEntityDescription, ValveControllerEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, api_category, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

PAIRED_SENSOR_DESCRIPTIONS: Incomplete
VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorSensor(PairedSensorEntity, SensorEntity):
    entity_description: PairedSensorDescription
    @property
    def native_value(self) -> StateType: ...

class ValveControllerSensor(ValveControllerEntity, SensorEntity):
    entity_description: ValveControllerSensorDescription
    @property
    def native_value(self) -> StateType: ...
