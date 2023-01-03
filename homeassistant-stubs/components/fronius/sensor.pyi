from . import FroniusSolarNet as FroniusSolarNet
from .const import DOMAIN as DOMAIN
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE_REACTIVE as POWER_VOLT_AMPERE_REACTIVE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

ENERGY_VOLT_AMPERE_REACTIVE_HOUR: Final[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

INVERTER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
LOGGER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
METER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
OHMPILOT_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
POWER_FLOW_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
STORAGE_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]

class _FroniusSensorEntity(CoordinatorEntity['FroniusCoordinatorBase'], SensorEntity):
    entity_descriptions: list[SensorEntityDescription]
    _attr_has_entity_name: bool
    entity_description: Incomplete
    solar_net_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: FroniusCoordinatorBase, key: str, solar_net_id: str) -> None: ...
    def _device_data(self) -> dict[str, Any]: ...
    def _get_entity_value(self) -> Any: ...
    def _handle_coordinator_update(self) -> None: ...

class InverterSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusInverterUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class LoggerSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_device_info: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusLoggerUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class MeterSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusMeterUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class OhmpilotSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusOhmpilotUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class PowerFlowSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusPowerFlowUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class StorageSensor(_FroniusSensorEntity):
    entity_descriptions: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FroniusStorageUpdateCoordinator, key: str, solar_net_id: str) -> None: ...
