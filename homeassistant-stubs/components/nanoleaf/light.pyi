from . import NanoleafEntryData as NanoleafEntryData
from .const import DOMAIN as DOMAIN
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

RESERVED_EFFECTS: Incomplete
DEFAULT_NAME: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafLight(NanoleafEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_icon: str
    _attr_unique_id: Incomplete
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator[None]) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def effect(self) -> str | None: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def hs_color(self) -> tuple[int, int]: ...
    @property
    def color_mode(self) -> ColorMode | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
