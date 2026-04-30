from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .entity import MusicAssistantPlayerOptionEntity as MusicAssistantPlayerOptionEntity
from .helpers import catch_musicassistant_error as catch_musicassistant_error
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from music_assistant_client.client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.player import PlayerOption as PlayerOption
from typing import Final

PLAYER_OPTIONS_SELECT: Final[dict[str, bool]]

async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MusicAssistantPlayerConfigSelect(MusicAssistantPlayerOptionEntity, SelectEntity):
    _option_translation_key_to_key_mapping: Incomplete
    _option_key_to_translation_key_mapping: Incomplete
    entity_description: Incomplete
    _attr_options: Incomplete
    def __init__(self, mass: MusicAssistantClient, player_id: str, player_option: PlayerOption, entity_description: SelectEntityDescription) -> None: ...
    @catch_musicassistant_error
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    def on_player_option_update(self, player_option: PlayerOption) -> None: ...
