from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .entity import MusicAssistantEntity as MusicAssistantEntity
from .helpers import catch_musicassistant_error as catch_musicassistant_error
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MusicAssistantFavoriteButton(MusicAssistantEntity, ButtonEntity):
    entity_description: Incomplete
    @catch_musicassistant_error
    async def async_press(self) -> None: ...
