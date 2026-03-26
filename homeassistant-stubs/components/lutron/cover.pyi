from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronDevice as LutronDevice
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import Output as Output
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronCover(LutronDevice, CoverEntity):
    _attr_supported_features: Incomplete
    _lutron_device: Output
    _attr_name: Incomplete
    def close_cover(self, **kwargs: Any) -> None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    def set_cover_position(self, **kwargs: Any) -> None: ...
    def _request_state(self) -> None: ...
    _attr_is_closed: Incomplete
    _attr_current_cover_position: Incomplete
    def _update_attrs(self) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
