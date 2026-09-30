from .const import DOMAIN as DOMAIN
from .coordinator import VitesyConfigEntry as VitesyConfigEntry, VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator, supports_mode as supports_mode
from .entity import VitesyEntity as VitesyEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VitesyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VitesyModeSelect(VitesyEntity, SelectEntity):
    _attr_translation_key: str
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VitesyDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
