from . import DuotecnoConfigEntry as DuotecnoConfigEntry
from .entity import DuotecnoEntity as DuotecnoEntity, api_call as api_call
from _typeshed import Incomplete
from duotecno.unit import DuoswitchUnit as DuoswitchUnit
from homeassistant.components.cover import CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DuotecnoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DuotecnoCover(DuotecnoEntity, CoverEntity):
    _unit: DuoswitchUnit
    _attr_supported_features: Incomplete
    @property
    def is_closed(self) -> bool | None: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @api_call
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @api_call
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
