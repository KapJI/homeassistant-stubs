from .coordinator import ValloxConfigEntry as ValloxConfigEntry, ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from datetime import date
from homeassistant.components.date import DateEntity as DateEntity
from homeassistant.const import CONF_NAME as CONF_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

class ValloxFilterChangeDateEntity(ValloxEntity, DateEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> date | None: ...
    async def async_set_value(self, value: date) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ValloxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
