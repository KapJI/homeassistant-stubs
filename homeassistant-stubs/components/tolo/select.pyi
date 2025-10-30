from .const import AromaTherapySlot as AromaTherapySlot, LampMode as LampMode
from .coordinator import ToloConfigEntry as ToloConfigEntry, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tololib import ToloClient as ToloClient, ToloSettings as ToloSettings

@dataclass(frozen=True, kw_only=True)
class ToloSelectEntityDescription(SelectEntityDescription):
    options: list[str]
    getter: Callable[[ToloSettings], str]
    setter: Callable[[ToloClient, str], bool]

SELECTS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ToloConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ToloSelectEntity(ToloSaunaCoordinatorEntity, SelectEntity):
    _attr_entity_category: Incomplete
    entity_description: ToloSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry, entity_description: ToloSelectEntityDescription) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str: ...
    def select_option(self, option: str) -> None: ...
