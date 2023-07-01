from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from jaraco.abode.devices.light import Light as AbodeLT
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeLight(AbodeDevice, LightEntity):
    _device: AbodeLT
    _attr_name: Incomplete
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_temp(self) -> int | None: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def color_mode(self) -> str | None: ...
    @property
    def supported_color_modes(self) -> set[str] | None: ...
