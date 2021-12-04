from . import EvilGeniusEntity as EvilGeniusEntity, EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .util import update_when_done as update_when_done
from homeassistant.components import light as light
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

HA_NO_EFFECT: str
FIB_NO_EFFECT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EvilGeniusLight(EvilGeniusEntity, light.LightEntity):
    _attr_supported_features: Any
    _attr_supported_color_modes: Any
    _attr_color_mode: Any
    _attr_unique_id: Any
    _attr_effect_list: Any
    def __init__(self, coordinator: EvilGeniusUpdateCoordinator) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def rgb_color(self) -> tuple[int, int, int]: ...
    @property
    def effect(self) -> str: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
