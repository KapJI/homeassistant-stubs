from .const import ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_METER_TYPE_NAME as ATTR_METER_TYPE_NAME, ATTR_VALUE as ATTR_VALUE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE, SERVICE_RESET_METER as SERVICE_RESET_METER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .discovery_data_template import NumericSensorDataTemplate as NumericSensorDataTemplate, NumericSensorDataTemplateData as NumericSensorDataTemplateData
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_device_id as get_device_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from collections.abc import Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.const import NodeStatus
from zwave_js_server.model.node import Node as ZwaveNode

LOGGER: Any
STATUS_ICON: dict[NodeStatus, str]
ENTITY_DESCRIPTION_KEY_MAP: dict[str, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSensorBase(ZWaveBaseEntity, SensorEntity):
    entity_description: Any
    _attr_native_unit_of_measurement: Any
    _attr_force_update: bool
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: Union[str, None] = ...) -> None: ...

class ZWaveStringSensor(ZwaveSensorBase):
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class ZWaveNumericSensor(ZwaveSensorBase):
    _attr_native_unit_of_measurement: Any
    def on_value_update(self) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class ZWaveMeterSensor(ZWaveNumericSensor):
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Union[int, str]], None]: ...
    async def async_reset_meter(self, meter_type: Union[int, None] = ..., value: Union[int, None] = ...) -> None: ...

class ZWaveListSensor(ZwaveSensorBase):
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: Union[str, None] = ...) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...

class ZWaveConfigParameterSensor(ZwaveSensorBase):
    _primary_value: Any
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, entity_description: SensorEntityDescription, unit_of_measurement: Union[str, None] = ...) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...

class ZWaveNodeStatusSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_entity_category: Any
    config_entry: Any
    client: Any
    node: Any
    _attr_name: Any
    _base_unique_id: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    _attr_native_value: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, node: ZwaveNode) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    def _status_changed(self, _: dict) -> None: ...
    @property
    def icon(self) -> Union[str, None]: ...
    async def async_added_to_hass(self) -> None: ...
