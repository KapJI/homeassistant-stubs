import re
from . import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from .const import DOMAIN as DOMAIN, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, SENSOR_KEYS as SENSOR_KEYS
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate, UnitOfFrequency as UnitOfFrequency, UnitOfInformation as UnitOfInformation, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

_LOGGER: Incomplete

def format_default(value: StateType) -> tuple[StateType, str | None]: ...
def format_freq_mhz(value: StateType) -> tuple[StateType, UnitOfFrequency]: ...
def format_last_reset_elapsed_seconds(value: str | None) -> datetime | None: ...
def signal_icon(limits: Sequence[int], value: StateType) -> str: ...
def bandwidth_icon(limits: Sequence[int], value: StateType) -> str: ...

class HuaweiSensorGroup:
    descriptions: dict[str, HuaweiSensorEntityDescription]
    include: re.Pattern[str] | None
    exclude: re.Pattern[str] | None
    def __init__(self, descriptions, include, exclude) -> None: ...

class HuaweiSensorEntityDescription(SensorEntityDescription):
    name: str
    format_fn: Callable[[str], tuple[StateType, str | None]]
    icon_fn: Callable[[StateType], str] | None
    device_class_fn: Callable[[StateType], SensorDeviceClass | None] | None
    last_reset_item: str | None
    last_reset_format_fn: Callable[[str | None], datetime | None] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, format_fn, icon_fn, device_class_fn, last_reset_item, last_reset_format_fn) -> None: ...

SENSOR_META: dict[str, HuaweiSensorGroup]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HuaweiLteSensor(HuaweiLteBaseEntityWithDevice, SensorEntity):
    key: str
    item: str
    entity_description: HuaweiSensorEntityDescription
    _state: StateType
    _unit: str | None
    _last_reset: datetime | None
    _attr_name: Incomplete
    def __post_init__(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def last_reset(self) -> datetime | None: ...
    _available: Incomplete
    async def async_update(self) -> None: ...
    def __init__(self, router, key, item, entity_description) -> None: ...
