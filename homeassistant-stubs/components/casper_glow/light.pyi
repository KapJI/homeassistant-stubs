from .const import DEFAULT_DIMMING_TIME_MINUTES as DEFAULT_DIMMING_TIME_MINUTES, SORTED_BRIGHTNESS_LEVELS as SORTED_BRIGHTNESS_LEVELS
from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from .entity import CasperGlowEntity as CasperGlowEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from pycasperglow import GlowState as GlowState
from typing import Any

PARALLEL_UPDATES: int

def _ha_brightness_to_device_pct(brightness: int) -> int: ...
def _device_pct_to_ha_brightness(pct: int) -> int: ...
async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CasperGlowLight(CasperGlowEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_color_mode: Incomplete
    _attr_brightness: Incomplete
    @callback
    def _update_from_state(self, state: GlowState) -> None: ...
    @callback
    def _async_handle_state_update(self, state: GlowState) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
