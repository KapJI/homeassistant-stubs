from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from .helpers import setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode

PARALLEL_UPDATES: int
BUTTON_DESCRIPTIONS: dict[AttributeType, ButtonEntityDescription]

async def add_button_entities(config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, nodes: list[HomeeNode]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeButton(HomeeEntity, ButtonEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
