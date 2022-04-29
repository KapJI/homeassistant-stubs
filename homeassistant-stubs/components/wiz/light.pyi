from .const import DOMAIN as DOMAIN
from .entity import WizToggleEntity as WizToggleEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from pywizlight import PilotBuilder
from pywizlight.bulblibrary import BulbType as BulbType, Features as Features
from typing import Any

RGB_WHITE_CHANNELS_COLOR_MODE: Incomplete

def _async_pilot_builder(**kwargs: Any) -> PilotBuilder: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizBulbEntity(WizToggleEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_effect_list: Incomplete
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    _attr_brightness: Incomplete
    _attr_color_mode: Incomplete
    _attr_color_temp: Incomplete
    _attr_rgbww_color: Incomplete
    _attr_rgbw_color: Incomplete
    _attr_effect: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
