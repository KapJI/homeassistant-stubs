from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ColorMode as ColorMode, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from midealocal.devices.x13 import Midea13Device
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaLightEntityDescription(LightEntityDescription):
    models: list[DeviceType]

LIGHTS: list[MideaLightEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaLight(MideaEntity, LightEntity):
    _device: Midea13Device
    @property
    @override
    def supported_features(self) -> LightEntityFeature: ...
    @property
    @override
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    @override
    def color_mode(self) -> ColorMode: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def brightness(self) -> int | None: ...
    @property
    @override
    def color_temp_kelvin(self) -> int | None: ...
    @property
    @override
    def min_color_temp_kelvin(self) -> int: ...
    @property
    @override
    def max_color_temp_kelvin(self) -> int: ...
    @property
    @override
    def effect_list(self) -> list[str]: ...
    @property
    @override
    def effect(self) -> str | None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
