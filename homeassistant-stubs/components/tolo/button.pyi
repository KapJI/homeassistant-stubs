from .coordinator import ToloConfigEntry as ToloConfigEntry, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ToloConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ToloLampNextColorButton(ToloSaunaCoordinatorEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry) -> None: ...
    @property
    def available(self) -> bool: ...
    def press(self) -> None: ...
