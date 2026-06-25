from .coordinator import ImmichConfigEntry as ImmichConfigEntry, ImmichDataUpdateCoordinator as ImmichDataUpdateCoordinator
from .entity import ImmichEntity as ImmichEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ImmichConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ImmichUpdateEntity(ImmichEntity, UpdateEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ImmichDataUpdateCoordinator) -> None: ...
    @property
    @override
    def installed_version(self) -> str: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @property
    @override
    def release_url(self) -> str | None: ...
