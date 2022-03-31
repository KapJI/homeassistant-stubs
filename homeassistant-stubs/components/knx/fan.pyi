from .const import DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import FanSchema as FanSchema
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import FanEntity as FanEntity, SUPPORT_OSCILLATE as SUPPORT_OSCILLATE, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any, Final
from xknx import XKNX as XKNX
from xknx.devices import Fan as XknxFan

DEFAULT_PERCENTAGE: Final[int]

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXFan(KnxEntity, FanEntity):
    _device: XknxFan
    _step_range: Any
    _attr_entity_category: Any
    _attr_unique_id: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def percentage(self) -> Union[int, None]: ...
    @property
    def speed_count(self) -> int: ...
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def oscillating(self) -> Union[bool, None]: ...
