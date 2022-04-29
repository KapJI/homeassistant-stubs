from .const import POWER_PLUGS as POWER_PLUGS
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DOMAIN as DOMAIN, EFFECT_COLORLOOP as EFFECT_COLORLOOP, FLASH_LONG as FLASH_LONG, FLASH_SHORT as FLASH_SHORT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_hs_to_xy as color_hs_to_xy
from pydeconz.models.group import Group
from pydeconz.models.light.light import Light
from typing import Any, TypeVar, TypedDict

DECONZ_GROUP: str
EFFECT_TO_DECONZ: Incomplete
FLASH_TO_DECONZ: Incomplete
_L = TypeVar('_L', Group, Light)

class SetStateAttributes(TypedDict):
    alert: str
    brightness: int
    color_temperature: int
    effect: str
    hue: int
    on: bool
    saturation: int
    transition_time: int
    xy: tuple[float, float]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBaseLight(DeconzDevice, LightEntity):
    TYPE: Incomplete
    _device: _L
    _attr_supported_color_modes: Incomplete
    _attr_effect_list: Incomplete
    def __init__(self, device: _L, gateway: DeconzGateway) -> None: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def xy_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...

class DeconzLight(DeconzBaseLight[Light]):
    _device: Light
    @property
    def max_mireds(self) -> int: ...
    @property
    def min_mireds(self) -> int: ...

class DeconzGroup(DeconzBaseLight[Group]):
    _device: Group
    _unique_id: Incomplete
    def __init__(self, device: Group, gateway: DeconzGateway) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
