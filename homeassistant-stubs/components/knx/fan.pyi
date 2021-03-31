from .const import DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from homeassistant.components.fan import FanEntity as FanEntity, SUPPORT_OSCILLATE as SUPPORT_OSCILLATE, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any, Callable, Iterable
from xknx.devices import Fan as XknxFan

DEFAULT_PERCENTAGE: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXFan(KnxEntity, FanEntity):
    def __init__(self, device: XknxFan) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def percentage(self) -> Union[int, None]: ...
    @property
    def speed_count(self) -> int: ...
    async def async_turn_on(self, speed: Union[str, None]=..., percentage: Union[int, None]=..., preset_mode: Union[str, None]=..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def oscillating(self) -> Union[bool, None]: ...
