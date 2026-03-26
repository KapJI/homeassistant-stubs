from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronDevice as LutronDevice
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Output as Output
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronFan(LutronDevice, FanEntity):
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_speed_count: int
    _attr_supported_features: Incomplete
    _lutron_device: Output
    _prev_percentage: int | None
    def set_percentage(self, percentage: int) -> None: ...
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def _request_state(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_percentage: Incomplete
    def _update_attrs(self) -> None: ...
