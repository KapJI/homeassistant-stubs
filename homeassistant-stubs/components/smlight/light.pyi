from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysmlight.const import AmbiEffect
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(kw_only=True, frozen=True)
class SmLightEntityDescription(LightEntityDescription):
    effect_list: list[str]

AMBILIGHT: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmLightEntity(SmEntity, LightEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmLightEntityDescription
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_effect_list: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmLightEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_effect: Incomplete
    _attr_rgb_color: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_ambilight_changes(self, changes: dict) -> None: ...
    def _effect_from_mode(self, mode: AmbiEffect | None) -> str | None: ...
    def _parse_rgb_color(self, color: str | None) -> tuple[int, int, int] | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
