from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizLight(OverkizEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def rgb_color(self) -> Union[tuple[int, int, int], None]: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
