from . import RingData as RingData
from .const import DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingStickUpCam
from typing import Any

_LOGGER: Incomplete
SKIP_UPDATES_DELAY: Incomplete

class OnOffState(StrEnum):
    ON: Incomplete
    OFF: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingLight(RingEntity[RingStickUpCam], LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    _no_updates_until: Incomplete
    def __init__(self, device: RingStickUpCam, coordinator: RingDataCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _set_light(self, new_state: OnOffState) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
