import re
from . import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from .const import DOMAIN as DOMAIN, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, SENSOR_KEYS as SENSOR_KEYS
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfDataRate as UnitOfDataRate, UnitOfFrequency as UnitOfFrequency, UnitOfInformation as UnitOfInformation, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

_LOGGER: Incomplete

def format_default(value: StateType) -> tuple[StateType, Union[str, None]]: ...

class HuaweiSensorGroup:
    descriptions: dict[str, HuaweiSensorEntityDescription]
    include: Union[re.Pattern[str], None]
    exclude: Union[re.Pattern[str], None]
    def __init__(self, descriptions, include, exclude) -> None: ...

class HuaweiSensorEntityDescription(SensorEntityDescription):
    formatter: Callable[[str], tuple[StateType, Union[str, None]]]
    icon_fn: Union[Callable[[StateType], str], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, options, formatter, icon_fn) -> None: ...

SENSOR_META: dict[str, HuaweiSensorGroup]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HuaweiLteSensor(HuaweiLteBaseEntityWithDevice, SensorEntity):
    key: str
    item: str
    entity_description: HuaweiSensorEntityDescription
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
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    _available: Incomplete
    async def async_update(self) -> None: ...
    def __init__(self, router, key, item, entity_description) -> None: ...
