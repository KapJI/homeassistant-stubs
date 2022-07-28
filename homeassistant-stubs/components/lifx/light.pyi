from .const import DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .manager import LIFXManager as LIFXManager, SERVICE_EFFECT_COLORLOOP as SERVICE_EFFECT_COLORLOOP, SERVICE_EFFECT_PULSE as SERVICE_EFFECT_PULSE, SERVICE_EFFECT_STOP as SERVICE_EFFECT_STOP
from .util import convert_16_to_8 as convert_16_to_8, convert_8_to_16 as convert_8_to_16, find_hsbk as find_hsbk, lifx_features as lifx_features, merge_hsbk as merge_hsbk
from _typeshed import Incomplete
from homeassistant import util as util
from homeassistant.components.light import ATTR_EFFECT as ATTR_EFFECT, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LIGHT_TURN_ON_SCHEMA as LIGHT_TURN_ON_SCHEMA, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

SERVICE_LIFX_SET_STATE: str
COLOR_ZONE_POPULATE_DELAY: float
ATTR_INFRARED: str
ATTR_ZONES: str
ATTR_POWER: str
LIFX_SET_STATE_SCHEMA: Incomplete
HSBK_HUE: int
HSBK_SATURATION: int
HSBK_BRIGHTNESS: int
HSBK_KELVIN: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXLight(CoordinatorEntity[LIFXUpdateCoordinator], LightEntity):
    _attr_supported_features: Incomplete
    mac_addr: Incomplete
    bulb: Incomplete
    manager: Incomplete
    effects_conductor: Incomplete
    postponed_update: Incomplete
    entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    _attr_device_info: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, manager: LIFXManager, entry: ConfigEntry) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def effect(self) -> Union[str, None]: ...
    async def update_during_transition(self, when: int) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def set_state(self, **kwargs: Any) -> None: ...
    async def set_power(self, pwr: bool, duration: int = ...) -> None: ...
    async def set_color(self, hsbk: list[Union[float, int, None]], kwargs: dict[str, Any], duration: int = ...) -> None: ...
    async def get_color(self) -> None: ...
    async def default_effect(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class LIFXWhite(LIFXLight):
    _attr_effect_list: Incomplete

class LIFXColor(LIFXLight):
    _attr_effect_list: Incomplete
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...

class LIFXStrip(LIFXColor):
    async def set_color(self, hsbk: list[Union[float, int, None]], kwargs: dict[str, Any], duration: int = ...) -> None: ...
    async def update_color_zones(self) -> None: ...
