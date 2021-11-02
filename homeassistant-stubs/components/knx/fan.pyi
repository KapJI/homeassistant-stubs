from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import FanSchema as FanSchema
from homeassistant.components.fan import FanEntity as FanEntity, SUPPORT_OSCILLATE as SUPPORT_OSCILLATE, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any, Final
from xknx import XKNX as XKNX
from xknx.devices import Fan as XknxFan

DEFAULT_PERCENTAGE: Final[int]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class KNXFan(KnxEntity, FanEntity):
    _device: XknxFan
    _step_range: Any
    _attr_unique_id: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def percentage(self) -> Union[int, None]: ...
    @property
    def speed_count(self) -> int: ...
    async def async_turn_on(self, speed: Union[str, None] = ..., percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def oscillating(self) -> Union[bool, None]: ...
