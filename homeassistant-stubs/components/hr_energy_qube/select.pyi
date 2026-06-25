from . import QubeConfigEntry as QubeConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import QubeCoordinator as QubeCoordinator
from .entity import QubeEntity as QubeEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
SG_READY_OPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QubeSGReadySelect(QubeEntity, SelectEntity):
    _attr_options = SG_READY_OPTIONS
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QubeCoordinator, entry: QubeConfigEntry) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
