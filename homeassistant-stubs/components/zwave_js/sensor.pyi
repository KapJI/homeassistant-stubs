from .const import ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_METER_TYPE_NAME as ATTR_METER_TYPE_NAME, ATTR_VALUE as ATTR_VALUE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TIMESTAMP as ENTITY_DESC_KEY_TIMESTAMP, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE, SERVICE_RESET_METER as SERVICE_RESET_METER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_device_id as get_device_id
from collections.abc import Mapping
from homeassistant.components.sensor import DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_POWER_FACTOR as DEVICE_CLASS_POWER_FACTOR, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode

LOGGER: Any

class ZwaveSensorEntityDescription(SensorEntityDescription):
    info: Union[ZwaveDiscoveryInfo, None]

ENTITY_DESCRIPTION_KEY_MAP: dict[str, ZwaveSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSensorBase(ZWaveBaseEntity, SensorEntity):
    entity_description: Any
    _attr_force_update: bool
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, entity_description: ZwaveSensorEntityDescription) -> None: ...

class ZWaveStringSensor(ZwaveSensorBase):
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class ZWaveNumericSensor(ZwaveSensorBase):
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
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, entity_description: ZwaveSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...

class ZWaveConfigParameterSensor(ZwaveSensorBase):
    _primary_value: Any
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, entity_description: ZwaveSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...

class ZWaveNodeStatusSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_entity_registry_enabled_default: bool
    config_entry: Any
    client: Any
    node: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    _attr_native_value: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, node: ZwaveNode) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    def _status_changed(self, _: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
