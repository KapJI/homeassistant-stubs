from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, ROLE_GENERIC as ROLE_GENERIC
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc, get_entity_rpc_device_info as get_entity_rpc_device_info
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_blu_trv_device_info as get_blu_trv_device_info, get_device_entry_gen as get_device_entry_gen, get_device_uptime as get_device_uptime, get_shelly_air_lamp_life as get_shelly_air_lamp_life, get_virtual_component_unit as get_virtual_component_unit, is_rpc_wifi_stations_disabled as is_rpc_wifi_stations_disabled, is_view_for_platform as is_view_for_platform
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from dataclasses import dataclass
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class BlockSensorDescription(BlockEntityDescription, SensorEntityDescription): ...

@dataclass(frozen=True, kw_only=True)
class RpcSensorDescription(RpcEntityDescription, SensorEntityDescription):
    emeter_phase: str | None = ...

@dataclass(frozen=True, kw_only=True)
class RestSensorDescription(RestEntityDescription, SensorEntityDescription): ...

class RpcSensor(ShellyRpcAttributeEntity, SensorEntity):
    entity_description: RpcSensorDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class RpcEnergyConsumedSensor(RpcSensor):
    @property
    def native_value(self) -> StateType: ...

class RpcPresenceSensor(RpcSensor):
    @property
    def available(self) -> bool: ...

class RpcEmeterPhaseSensor(RpcSensor):
    entity_description: RpcSensorDescription
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSensorDescription) -> None: ...

class RpcBluTrvSensor(RpcSensor):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSensorDescription) -> None: ...

SENSORS: dict[tuple[str, str], BlockSensorDescription]
REST_SENSORS: Final[Incomplete]
RPC_SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockSensor(ShellyBlockAttributeEntity, SensorEntity):
    entity_description: BlockSensorDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class RestSensor(ShellyRestAttributeEntity, SensorEntity):
    entity_description: RestSensorDescription
    @property
    def native_value(self) -> StateType: ...

class BlockSleepingSensor(ShellySleepingBlockAttributeEntity, RestoreSensor):
    entity_description: BlockSensorDescription
    restored_data: SensorExtraStoredData | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockSensorDescription, entry: RegistryEntry | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...

class RpcSleepingSensor(ShellySleepingRpcAttributeEntity, RestoreSensor):
    entity_description: RpcSensorDescription
    restored_data: SensorExtraStoredData | None
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSensorDescription, entry: RegistryEntry | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
