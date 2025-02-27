from . import TPLinkConfigEntry as TPLinkConfigEntry, legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription, LightEntityFeature as LightEntityFeature, filter_supported_color_modes as filter_supported_color_modes
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from kasa import Device as Device
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete
SERVICE_RANDOM_EFFECT: str
SERVICE_SEQUENCE_EFFECT: str
HUE: Incomplete
SAT: Incomplete
VAL: Incomplete
TRANSITION: Incomplete
HSV_SEQUENCE: Incomplete
BASE_EFFECT_DICT: VolDictType
SEQUENCE_EFFECT_DICT: VolDictType
RANDOM_EFFECT_DICT: VolDictType

@callback
def _async_build_base_effect(brightness: int, duration: int, transition: int, segments: list[int]) -> dict[str, Any]: ...
def _get_backwards_compatible_light_unique_id(device: Device, entity_description: TPLinkModuleEntityDescription) -> str: ...

@dataclass(frozen=True, kw_only=True)
class TPLinkLightEntityDescription(LightEntityDescription, TPLinkModuleEntityDescription):
    unique_id_fn = _get_backwards_compatible_light_unique_id

LIGHT_DESCRIPTIONS: tuple[TPLinkLightEntityDescription, ...]
LIGHT_EFFECT_DESCRIPTIONS: tuple[TPLinkLightEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkLightEntity(CoordinatedTPLinkModuleEntity, LightEntity):
    _attr_supported_features: Incomplete
    _fixed_color_mode: ColorMode | None
    entity_description: TPLinkLightEntityDescription
    _light_module: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkLightEntityDescription, *, parent: Device | None = None) -> None: ...
    @callback
    def _async_extract_brightness_transition(self, **kwargs: Any) -> tuple[int | None, int | None]: ...
    async def _async_set_hsv(self, hs_color: tuple[int, int], brightness: int | None, transition: int | None) -> None: ...
    async def _async_set_color_temp(self, color_temp: float, brightness: int | None, transition: int | None) -> None: ...
    async def _async_turn_on_with_brightness(self, brightness: int | None, transition: int | None) -> None: ...
    @async_refresh_after
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _determine_color_mode(self) -> ColorMode: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_color_mode: Incomplete
    _attr_color_temp_kelvin: Incomplete
    _attr_hs_color: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...

class TPLinkLightEffectEntity(TPLinkLightEntity):
    _attr_supported_features: Incomplete
    _effect_module: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkLightEntityDescription, *, parent: Device | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _register_effects_services(self) -> None: ...
    _attr_effect: Incomplete
    _attr_color_mode: Incomplete
    _attr_effect_list: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
    @async_refresh_after
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_set_random_effect(self, brightness: int, duration: int, transition: int, segments: list[int], fadeoff: int, init_states: tuple[int, int, int], random_seed: int, backgrounds: Sequence[tuple[int, int, int]] | None = None, hue_range: tuple[int, int] | None = None, saturation_range: tuple[int, int] | None = None, brightness_range: tuple[int, int] | None = None, transition_range: tuple[int, int] | None = None) -> None: ...
    async def async_set_sequence_effect(self, brightness: int, duration: int, transition: int, segments: list[int], sequence: Sequence[tuple[int, int, int]], repeat_times: int, spread: int, direction: int) -> None: ...
