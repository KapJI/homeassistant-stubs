from . import FroniusConfigEntry as FroniusConfigEntry
from .const import DOMAIN as DOMAIN, InverterStatusCodeOption as InverterStatusCodeOption, MeterLocationCodeOption as MeterLocationCodeOption, OhmPilotStateCodeOption as OhmPilotStateCodeOption, SOLAR_NET_DISCOVERY_NEW as SOLAR_NET_DISCOVERY_NEW, get_inverter_status_message as get_inverter_status_message, get_meter_location_description as get_meter_location_description, get_ohmpilot_state_message as get_ohmpilot_state_message
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE_REACTIVE as POWER_VOLT_AMPERE_REACTIVE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

ENERGY_VOLT_AMPERE_REACTIVE_HOUR: Final[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: FroniusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class FroniusSensorEntityDescription(SensorEntityDescription):
    default_value: StateType | None = ...
    invalid_when_falsy: bool = ...
    response_key: str | None = ...
    value_fn: Callable[[StateType], StateType] | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, default_value, invalid_when_falsy, response_key, value_fn) -> None: ...

INVERTER_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]
LOGGER_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]
METER_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]
OHMPILOT_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]
POWER_FLOW_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]
STORAGE_ENTITY_DESCRIPTIONS: list[FroniusSensorEntityDescription]

class _FroniusSensorEntity(CoordinatorEntity['FroniusCoordinatorBase'], SensorEntity):
    entity_description: FroniusSensorEntityDescription
    _attr_has_entity_name: bool
    response_key: Incomplete
    solar_net_id: Incomplete
    _attr_native_value: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: FroniusCoordinatorBase, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...
    def _device_data(self) -> dict[str, Any]: ...
    def _get_entity_value(self) -> Any: ...
    def _handle_coordinator_update(self) -> None: ...

class InverterSensor(_FroniusSensorEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusInverterUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...

class LoggerSensor(_FroniusSensorEntity):
    _attr_device_info: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusLoggerUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...

class MeterSensor(_FroniusSensorEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusMeterUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...

class OhmpilotSensor(_FroniusSensorEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusOhmpilotUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...

class PowerFlowSensor(_FroniusSensorEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusPowerFlowUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...

class StorageSensor(_FroniusSensorEntity):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FroniusStorageUpdateCoordinator, description: FroniusSensorEntityDescription, solar_net_id: str) -> None: ...
