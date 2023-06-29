from .const import ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_METER_TYPE_NAME as ATTR_METER_TYPE_NAME, ATTR_VALUE as ATTR_VALUE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_PRODUCTION_POWER as ENTITY_DESC_KEY_ENERGY_PRODUCTION_POWER, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TIME as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TIME, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TODAY as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TODAY, ENTITY_DESC_KEY_ENERGY_PRODUCTION_TOTAL as ENTITY_DESC_KEY_ENERGY_PRODUCTION_TOTAL, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_UV_INDEX as ENTITY_DESC_KEY_UV_INDEX, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE, LOGGER as LOGGER, SERVICE_RESET_METER as SERVICE_RESET_METER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .discovery_data_template import NumericSensorDataTemplate as NumericSensorDataTemplate, NumericSensorDataTemplateData as NumericSensorDataTemplateData
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_device_info as get_device_info, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UV_INDEX as UV_INDEX, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType, UNDEFINED as UNDEFINED
from zwave_js_server.const import NodeStatus
from zwave_js_server.model.controller import Controller
from zwave_js_server.model.controller.statistics import ControllerStatisticsDataType as ControllerStatisticsDataType
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.node.statistics import NodeStatisticsDataType as NodeStatisticsDataType

PARALLEL_UPDATES: int
STATUS_ICON: dict[NodeStatus, str]
ENTITY_DESCRIPTION_KEY_DEVICE_CLASS_MAP: dict[tuple[str, str], SensorEntityDescription]
ENTITY_DESCRIPTION_KEY_MAP: Incomplete
ENTITY_DESCRIPTION_CONTROLLER_STATISTICS_LIST: Incomplete
ENTITY_DESCRIPTION_NODE_STATISTICS_LIST: Incomplete

def get_entity_description(data: NumericSensorDataTemplateData) -> SensorEntityDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSensor(ZWaveBaseEntity, SensorEntity):
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_force_update: bool
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: str | None = ...) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...

class ZWaveNumericSensor(ZwaveSensor):
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def on_value_update(self) -> None: ...
    @property
    def native_value(self) -> float: ...

class ZWaveMeterSensor(ZWaveNumericSensor):
    @property
    def extra_state_attributes(self) -> Mapping[str, int | str] | None: ...
    async def async_reset_meter(self, meter_type: int | None = ..., value: int | None = ...) -> None: ...

class ZWaveListSensor(ZwaveSensor):
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: str | None = ...) -> None: ...
    @property
    def options(self) -> list[str] | None: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...

class ZWaveConfigParameterSensor(ZWaveListSensor):
    _attr_entity_category: Incomplete
    _primary_value: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: str | None = ...) -> None: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...

class ZWaveNodeStatusSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    config_entry: Incomplete
    node: Incomplete
    _attr_name: str
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, node: ZwaveNode) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    _attr_native_value: Incomplete
    def _status_changed(self, _: dict) -> None: ...
    @property
    def icon(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...

class ZWaveStatisticsSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_has_entity_name: bool
    entity_description: Incomplete
    config_entry: Incomplete
    statistics_src: Incomplete
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, statistics_src: ZwaveNode | Controller, description: SensorEntityDescription) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    def _get_data_from_statistics(self, statistics: ControllerStatisticsDataType | NodeStatisticsDataType) -> int | None: ...
    _attr_native_value: Incomplete
    def statistics_updated(self, event_data: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
