from . import KNXModule as KNXModule
from .const import ATTR_SOURCE as ATTR_SOURCE, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import SensorSchema as SensorSchema
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any
from xknx import XKNX as XKNX
from xknx.core.connection_state import XknxConnectionState
from xknx.devices import Sensor as XknxSensor

SCAN_INTERVAL: Incomplete

@dataclass(frozen=True)
class KNXSystemEntityDescription(SensorEntityDescription):
    always_available: bool = ...
    entity_category: EntityCategory = ...
    has_entity_name: bool = ...
    should_poll: bool = ...
    value_fn: Callable[[KNXModule], StateType | datetime] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, always_available, should_poll, value_fn) -> None: ...

SYSTEM_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_sensor(xknx: XKNX, config: ConfigType) -> XknxSensor: ...

class KNXSensor(KnxEntity, SensorEntity):
    _device: XknxSensor
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

class KNXSystemSensor(SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
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
    async def after_update_callback(self, _: XknxConnectionState) -> None: ...
    async def async_added_to_hass(self) -> None: ...
