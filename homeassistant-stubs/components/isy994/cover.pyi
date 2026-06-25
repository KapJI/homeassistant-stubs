from .const import UOM_8_BIT_RANGE as UOM_8_BIT_RANGE, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity, ISYProgramEntity as ISYProgramEntity
from .models import IsyConfigEntry as IsyConfigEntry
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: IsyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ISYCoverEntity(ISYNodeEntity, CoverEntity):
    _attr_supported_features: Incomplete
    @property
    @override
    def current_cover_position(self) -> int | None: ...
    @property
    @override
    def is_closed(self) -> bool | None: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...

class ISYCoverProgramEntity(ISYProgramEntity, CoverEntity):
    @property
    @override
    def is_closed(self) -> bool: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
