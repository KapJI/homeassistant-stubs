from . import FroniusSolarNet as FroniusSolarNet
from .const import DOMAIN as DOMAIN
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_RESOURCE as CONF_RESOURCE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE as POWER_VOLT_AMPERE, POWER_VOLT_AMPERE_REACTIVE as POWER_VOLT_AMPERE_REACTIVE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

_LOGGER: Final[Any]
ELECTRIC_CHARGE_AMPERE_HOURS: Final[str]
ENERGY_VOLT_AMPERE_REACTIVE_HOUR: Final[str]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

INVERTER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
LOGGER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
METER_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
OHMPILOT_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
POWER_FLOW_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]
STORAGE_ENTITY_DESCRIPTIONS: list[SensorEntityDescription]

class _FroniusSensorEntity(CoordinatorEntity, SensorEntity):
    coordinator: FroniusCoordinatorBase
    entity_descriptions: list[SensorEntityDescription]
    _entity_id_prefix: str
    entity_description: Any
    entity_id: Any
    solar_net_id: Any
    _attr_native_value: Any
    def __init__(self, coordinator: FroniusCoordinatorBase, key: str, solar_net_id: str) -> None: ...
    def _device_data(self) -> dict[str, Any]: ...
    def _get_entity_value(self) -> Any: ...
    def _handle_coordinator_update(self) -> None: ...

class InverterSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: FroniusInverterUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class LoggerSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: str
    _attr_device_info: Any
    _attr_native_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: FroniusLoggerUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class MeterSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: FroniusMeterUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class OhmpilotSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: FroniusOhmpilotUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class PowerFlowSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: str
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: FroniusPowerFlowUpdateCoordinator, key: str, solar_net_id: str) -> None: ...

class StorageSensor(_FroniusSensorEntity):
    entity_descriptions: Any
    _entity_id_prefix: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: FroniusStorageUpdateCoordinator, key: str, solar_net_id: str) -> None: ...
