from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .entity import MusicAssistantPlayerOptionEntity as MusicAssistantPlayerOptionEntity
from .helpers import catch_musicassistant_error as catch_musicassistant_error
from _typeshed import Incomplete
from homeassistant.components.text import TextEntity as TextEntity, TextEntityDescription as TextEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from music_assistant_client.client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.player import PlayerOption as PlayerOption
from typing import Final

PLAYER_OPTIONS_TEXT: Final[dict[str, bool]]

async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MusicAssistantPlayerConfigText(MusicAssistantPlayerOptionEntity, TextEntity):
    entity_description: Incomplete
    def __init__(self, mass: MusicAssistantClient, player_id: str, player_option: PlayerOption, entity_description: TextEntityDescription) -> None: ...
    @catch_musicassistant_error
    async def async_set_value(self, value: str) -> None: ...
    _attr_native_value: Incomplete
    def on_player_option_update(self, player_option: PlayerOption) -> None: ...
