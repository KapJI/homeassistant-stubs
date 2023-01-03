import re
from . import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from .const import DOMAIN as DOMAIN, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, SENSOR_KEYS as SENSOR_KEYS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DATA_BYTES as DATA_BYTES, DATA_RATE_BYTES_PER_SECOND as DATA_RATE_BYTES_PER_SECOND, FREQUENCY_MEGAHERTZ as FREQUENCY_MEGAHERTZ, PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import NamedTuple

_LOGGER: Incomplete

class SensorMeta(NamedTuple):
    name: Union[str, None]
    device_class: Union[SensorDeviceClass, None]
    icon: Union[str, Callable[[StateType], str], None]
    native_unit_of_measurement: Union[str, None]
    state_class: Union[SensorStateClass, None]
    entity_registry_enabled_default: bool
    entity_category: Union[EntityCategory, None]
    include: Union[re.Pattern[str], None]
    exclude: Union[re.Pattern[str], None]
    formatter: Union[Callable[[str], tuple[StateType, Union[str, None]]], None]

SENSOR_META: dict[Union[str, tuple[str, str]], SensorMeta]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def format_default(value: StateType) -> tuple[StateType, Union[str, None]]: ...

class HuaweiLteSensor(HuaweiLteBaseEntityWithDevice, SensorEntity):
    key: str
    item: str
    meta: SensorMeta
    _state: StateType
    _unit: Union[str, None]
    _attr_name: Incomplete
    def __post_init__(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def device_class(self) -> Union[SensorDeviceClass, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def state_class(self) -> Union[SensorStateClass, None]: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    _available: Incomplete
    async def async_update(self) -> None: ...
    @property
    def entity_category(self) -> Union[EntityCategory, None]: ...
    def __init__(self, router, key, item, meta) -> None: ...
