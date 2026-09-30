from .const import ATTR_INFRARED as ATTR_INFRARED, ATTR_POWER as ATTR_POWER, ATTR_ZONES as ATTR_ZONES, DATA_LIFX_MANAGER as DATA_LIFX_MANAGER, DOMAIN as DOMAIN, INFRARED_BRIGHTNESS as INFRARED_BRIGHTNESS, LOGGER as LOGGER, SERVICE_EFFECT_COLORLOOP as SERVICE_EFFECT_COLORLOOP, SERVICE_EFFECT_FLAME as SERVICE_EFFECT_FLAME, SERVICE_EFFECT_MORPH as SERVICE_EFFECT_MORPH, SERVICE_EFFECT_MOVE as SERVICE_EFFECT_MOVE, SERVICE_EFFECT_PULSE as SERVICE_EFFECT_PULSE, SERVICE_EFFECT_SKY as SERVICE_EFFECT_SKY, SERVICE_EFFECT_STOP as SERVICE_EFFECT_STOP
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from .manager import LIFXManager as LIFXManager
from .util import device_error as device_error, find_hsbk as find_hsbk, overwrites_existing_color as overwrites_existing_color, parse_hsbk_changes as parse_hsbk_changes, replace_hsbk as replace_hsbk
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_BRIGHTNESS_STEP as ATTR_BRIGHTNESS_STEP, ATTR_BRIGHTNESS_STEP_PCT as ATTR_BRIGHTNESS_STEP_PCT, ATTR_EFFECT as ATTR_EFFECT, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from lifx import HSBK as HSBK, Light, MatrixLight, MultiZoneLight
from typing import Any, override

PARALLEL_UPDATES: int
LIFX_STATE_SETTLE_DELAY: float
LIFX_MIN_COLOR_RAMP: float

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXLight(LIFXEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_effect_list: Incomplete
    device: Light
    manager: Incomplete
    postponed_update: CALLBACK_TYPE | None
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, manager: LIFXManager) -> None: ...
    @property
    @override
    def brightness(self) -> int: ...
    @property
    @override
    def color_temp_kelvin(self) -> int | None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def effect(self) -> str | None: ...
    async def update_during_transition(self, duration: float) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def set_state(self, **kwargs: Any) -> None: ...
    async def _async_set_deprecated_infrared(self, kwargs: dict[str, Any]) -> None: ...
    def _resolve_brightness_step(self, kwargs: dict[str, Any]) -> None: ...
    async def set_hev_cycle_state(self, power: bool, duration: float | None = None) -> None: ...
    async def set_power(self, pwr: bool, duration: float = 0.0) -> None: ...
    async def set_color(self, hsbk: HSBK, kwargs: dict[str, Any], duration: float = 0.0) -> None: ...
    async def default_effect(self, **kwargs: Any) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    def _cancel_postponed_update(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...

class LIFXColor(LIFXLight):
    _attr_effect_list: Incomplete
    @property
    @override
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    @override
    def color_mode(self) -> ColorMode: ...
    @property
    @override
    def hs_color(self) -> tuple[float, float] | None: ...
    async def async_refresh_before_merge(self) -> None: ...

class LIFXHevLight(LIFXColor):
    @override
    async def set_hev_cycle_state(self, power: bool, duration: float | None = None) -> None: ...

class LIFXMultiZone(LIFXColor):
    device: MultiZoneLight
    _attr_effect_list: Incomplete
    @override
    async def set_color(self, hsbk: HSBK, kwargs: dict[str, Any], duration: float = 0.0) -> None: ...

class LIFXMatrix(LIFXColor):
    device: MatrixLight
    _attr_effect_list: Incomplete
    @override
    async def set_color(self, hsbk: HSBK, kwargs: dict[str, Any], duration: float = 0.0) -> None: ...

class LIFXCeiling(LIFXMatrix):
    _attr_effect_list: Incomplete
