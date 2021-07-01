import re
from . import HuaweiLteBaseEntity as HuaweiLteBaseEntity
from .const import DOMAIN as DOMAIN, KEY_DEVICE_INFORMATION as KEY_DEVICE_INFORMATION, KEY_DEVICE_SIGNAL as KEY_DEVICE_SIGNAL, KEY_MONITORING_CHECK_NOTIFICATIONS as KEY_MONITORING_CHECK_NOTIFICATIONS, KEY_MONITORING_MONTH_STATISTICS as KEY_MONITORING_MONTH_STATISTICS, KEY_MONITORING_STATUS as KEY_MONITORING_STATUS, KEY_MONITORING_TRAFFIC_STATISTICS as KEY_MONITORING_TRAFFIC_STATISTICS, KEY_NET_CURRENT_PLMN as KEY_NET_CURRENT_PLMN, KEY_NET_NET_MODE as KEY_NET_NET_MODE, KEY_SMS_SMS_COUNT as KEY_SMS_SMS_COUNT, SENSOR_KEYS as SENSOR_KEYS
from homeassistant.components.sensor import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL, DATA_BYTES as DATA_BYTES, DATA_RATE_BYTES_PER_SECOND as DATA_RATE_BYTES_PER_SECOND, PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Callable, NamedTuple

_LOGGER: Any

class SensorMeta(NamedTuple):
    name: Union[str, None]
    device_class: Union[str, None]
    icon: Union[str, Callable[[StateType], str], None]
    unit: Union[str, None]
    enabled_default: bool
    include: Union[re.Pattern[str], None]
    exclude: Union[re.Pattern[str], None]
    formatter: Union[Callable[[str], tuple[StateType, Union[str, None]]], None]

SENSOR_META: dict[Union[str, tuple[str, str]], SensorMeta]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def format_default(value: StateType) -> tuple[StateType, Union[str, None]]: ...

class HuaweiLteSensor(HuaweiLteBaseEntity, SensorEntity):
    key: str
    item: str
    meta: SensorMeta
    _state: StateType
    _unit: Union[str, None]
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def state(self) -> StateType: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    _available: Any
    async def async_update(self) -> None: ...
    def __init__(self, router, available, unsub_handlers, key, item, meta, state, unit) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
