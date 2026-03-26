from . import LutronConfigEntry as LutronConfigEntry
from .const import CONF_DEFAULT_DIMMER_LEVEL as CONF_DEFAULT_DIMMER_LEVEL, DEFAULT_DIMMER_LEVEL as DEFAULT_DIMMER_LEVEL
from .entity import LutronDevice as LutronDevice
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_FLASH as ATTR_FLASH, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Lutron as Lutron, LutronEntity as LutronEntity, Output as Output
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def to_lutron_level(level: int) -> float: ...
def to_hass_level(level: float) -> int: ...

class LutronLight(LutronDevice, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _lutron_device: Output
    _prev_brightness: int | None
    _attr_name: Incomplete
    _config_entry: Incomplete
    def __init__(self, area_name: str, lutron_device: LutronEntity, controller: Lutron, config_entry: ConfigEntry) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    def _request_state(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    def _update_attrs(self) -> None: ...
