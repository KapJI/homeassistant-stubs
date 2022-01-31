import abc
from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxEntity as FluxEntity
from .util import _effect_brightness as _effect_brightness
from abc import abstractmethod
from homeassistant import config_entries as config_entries
from homeassistant.components.light import EFFECT_RANDOM as EFFECT_RANDOM
from homeassistant.components.number import NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Any
DEBOUNCE_TIME: int

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxSpeedNumber(FluxEntity, CoordinatorEntity, NumberEntity):
    _attr_min_value: int
    _attr_max_value: int
    _attr_step: int
    _attr_mode: Any
    _attr_icon: str
    @property
    def value(self) -> float: ...
    async def async_set_value(self, value: float) -> None: ...

class FluxConfigNumber(FluxEntity, CoordinatorEntity, NumberEntity, metaclass=abc.ABCMeta):
    _attr_entity_category: Any
    _attr_min_value: int
    _attr_step: int
    _attr_mode: Any
    _debouncer: Any
    _pending_value: Any
    def __init__(self, coordinator: FluxLedUpdateCoordinator, base_unique_id: str, name: str, key: Union[str, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_value(self, value: float) -> None: ...
    @abstractmethod
    async def _async_set_value(self) -> None: ...
    def _pixels_and_segments_fit_in_music_mode(self) -> bool: ...

class FluxPixelsPerSegmentNumber(FluxConfigNumber):
    _attr_icon: str
    @property
    def max_value(self) -> int: ...
    @property
    def value(self) -> int: ...
    async def _async_set_value(self) -> None: ...

class FluxSegmentsNumber(FluxConfigNumber):
    _attr_icon: str
    @property
    def max_value(self) -> int: ...
    @property
    def value(self) -> int: ...
    async def _async_set_value(self) -> None: ...

class FluxMusicNumber(FluxConfigNumber, metaclass=abc.ABCMeta):
    @property
    def available(self) -> bool: ...

class FluxMusicPixelsPerSegmentNumber(FluxMusicNumber):
    _attr_icon: str
    @property
    def max_value(self) -> int: ...
    @property
    def value(self) -> int: ...
    async def _async_set_value(self) -> None: ...

class FluxMusicSegmentsNumber(FluxMusicNumber):
    _attr_icon: str
    @property
    def max_value(self) -> int: ...
    @property
    def value(self) -> int: ...
    async def _async_set_value(self) -> None: ...
