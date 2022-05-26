from . import FritzBoxEntity as FritzBoxEntity
from .const import COLOR_MODE as COLOR_MODE, COLOR_TEMP_MODE as COLOR_TEMP_MODE, CONF_COORDINATOR as CONF_COORDINATOR, LOGGER as LOGGER
from .coordinator import FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import color as color
from typing import Any

SUPPORTED_COLOR_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxLight(FritzBoxEntity, LightEntity):
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    _supported_hs: Incomplete
    def __init__(self, coordinator: FritzboxDataUpdateCoordinator, ain: str, supported_colors: dict, supported_color_temps: list[str]) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
