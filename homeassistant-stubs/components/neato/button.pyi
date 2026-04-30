from . import NeatoConfigEntry as NeatoConfigEntry
from .entity import NeatoEntity as NeatoEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pybotvac import Robot as Robot

async def async_setup_entry(hass: HomeAssistant, entry: NeatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NeatoDismissAlertButton(NeatoEntity, ButtonEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, robot: Robot) -> None: ...
    async def async_press(self) -> None: ...
