from .const import ATTR_METER_TYPE as ATTR_METER_TYPE, ATTR_VALUE as ATTR_VALUE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, SERVICE_RESET_METER as SERVICE_RESET_METER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_device_id as get_device_id
from homeassistant.components.sensor import ATTR_LAST_RESET as ATTR_LAST_RESET, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.util import dt as dt
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.node import Node as ZwaveNode

LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSensorBase(ZWaveBaseEntity, SensorEntity):
    _attr_name: Any
    _attr_device_class: Any
    _attr_state_class: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    def _get_device_class(self) -> Union[str, None]: ...
    def _get_state_class(self) -> Union[str, None]: ...
    @property
    def force_update(self) -> bool: ...

class ZWaveStringSensor(ZwaveSensorBase):
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...

class ZWaveNumericSensor(ZwaveSensorBase):
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def state(self) -> float: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...

class ZWaveMeterSensor(ZWaveNumericSensor, RestoreEntity):
    _attr_state_class: Any
    _attr_last_reset: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    def async_update_last_reset(self, node: ZwaveNode, endpoint: int, meter_type: Union[int, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_reset_meter(self, meter_type: Union[int, None] = ..., value: Union[int, None] = ...) -> None: ...

class ZWaveListSensor(ZwaveSensorBase):
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...

class ZWaveConfigParameterSensor(ZwaveSensorBase):
    _primary_value: Any
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
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
    _attr_state: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, node: ZwaveNode) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    def _status_changed(self, _: dict) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
