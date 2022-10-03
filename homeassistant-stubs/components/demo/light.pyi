from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

LIGHT_COLORS: Incomplete
LIGHT_EFFECT_LIST: Incomplete
LIGHT_TEMPS: Incomplete
SUPPORT_DEMO: Incomplete
SUPPORT_DEMO_HS_WHITE: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoLight(LightEntity):
    _attr_should_poll: bool
    _available: bool
    _brightness: Incomplete
    _ct: Incomplete
    _effect: Incomplete
    _effect_list: Incomplete
    _features: int
    _hs_color: Incomplete
    _attr_name: Incomplete
    _rgbw_color: Incomplete
    _rgbww_color: Incomplete
    _state: Incomplete
    _unique_id: Incomplete
    _color_mode: Incomplete
    _color_modes: Incomplete
    def __init__(self, unique_id: str, name: str, state: bool, available: bool = ..., brightness: int = ..., ct: Union[int, None] = ..., effect_list: Union[list[str], None] = ..., effect: Union[str, None] = ..., hs_color: Union[tuple[int, int], None] = ..., rgbw_color: Union[tuple[int, int, int, int], None] = ..., rgbww_color: Union[tuple[int, int, int, int, int], None] = ..., supported_color_modes: Union[set[ColorMode], None] = ...) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def hs_color(self) -> Union[tuple[int, int], None]: ...
    @property
    def rgbw_color(self) -> Union[tuple[int, int, int, int], None]: ...
    @property
    def rgbww_color(self) -> Union[tuple[int, int, int, int, int], None]: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def effect_list(self) -> Union[list[str], None]: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
