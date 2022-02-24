from .const import DOMAIN as DOMAIN
from .entity import WizToggleEntity as WizToggleEntity
from .models import WizData as WizData
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_RGBW as COLOR_MODE_RGBW, COLOR_MODE_RGBWW as COLOR_MODE_RGBWW, LightEntity as LightEntity, SUPPORT_EFFECT as SUPPORT_EFFECT
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from pywizlight import PilotBuilder
from pywizlight.bulblibrary import BulbType as BulbType, Features as Features
from typing import Any

RGB_WHITE_CHANNELS_COLOR_MODE: Any

def _async_pilot_builder(**kwargs: Any) -> PilotBuilder: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizBulbEntity(WizToggleEntity, LightEntity):
    _attr_supported_color_modes: Any
    _attr_effect_list: Any
    _attr_min_mireds: Any
    _attr_max_mireds: Any
    _attr_supported_features: Any
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    _attr_brightness: Any
    _attr_color_mode: Any
    _attr_color_temp: Any
    _attr_rgbww_color: Any
    _attr_rgbw_color: Any
    _attr_effect: Any
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
