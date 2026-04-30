from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from .helpers import elgato_exception_handler as elgato_exception_handler
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElgatoLight(ElgatoEntity, LightEntity):
    _attr_name: Incomplete
    _attr_min_color_temp_kelvin: int
    _attr_max_color_temp_kelvin: int
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def color_temp_kelvin(self) -> int | None: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def is_on(self) -> bool: ...
    @elgato_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @elgato_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @elgato_exception_handler
    async def async_identify(self) -> None: ...
