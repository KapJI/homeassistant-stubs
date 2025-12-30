from .const import ATTR_SOURCE as ATTR_SOURCE, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY
from .dpt import get_supported_dpts as get_supported_dpts
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, _KnxEntityBase as _KnxEntityBase
from .knx_module import KNXModule as KNXModule
from .schema import SensorSchema as SensorSchema
from .storage.const import CONF_ALWAYS_CALLBACK as CONF_ALWAYS_CALLBACK, CONF_ENTITY as CONF_ENTITY, CONF_GA_SENSOR as CONF_GA_SENSOR
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, EntityCategory as EntityCategory, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any
from xknx.core.connection_state import XknxConnectionState
from xknx.devices import Device as XknxDevice, Sensor as XknxSensor

SCAN_INTERVAL: Incomplete

@dataclass(frozen=True)
class KNXSystemEntityDescription(SensorEntityDescription):
    always_available: bool = ...
    entity_category: EntityCategory = ...
    has_entity_name: bool = ...
    should_poll: bool = ...
    value_fn: Callable[[KNXModule], StateType | datetime] = ...

SYSTEM_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxSensor(RestoreSensor, _KnxEntityBase):
    _device: XknxSensor
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def after_update_callback(self, device: XknxDevice) -> None: ...

class KnxYamlSensor(_KnxSensor, KnxYamlEntity):
    _device: XknxSensor
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiSensor(_KnxSensor, KnxUiEntity):
    _device: XknxSensor
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_force_update: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...

class KNXSystemSensor(SensorEntity):
    _attr_has_entity_name: bool
    entity_description: KNXSystemEntityDescription
    knx: Incomplete
    _attr_device_info: Incomplete
    _attr_should_poll: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx: KNXModule, description: KNXSystemEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def available(self) -> bool: ...
    def after_update_callback(self, device: XknxConnectionState) -> None: ...
    async def async_added_to_hass(self) -> None: ...
