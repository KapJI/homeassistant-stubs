from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .entity import MusicAssistantPlayerOptionEntity as MusicAssistantPlayerOptionEntity
from .helpers import catch_musicassistant_error as catch_musicassistant_error
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from music_assistant_client.client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.player import PlayerOption as PlayerOption
from typing import Any, Final

PLAYER_OPTIONS_SWITCH: Final[dict[str, bool]]

async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MusicAssistantPlayerConfigSwitch(MusicAssistantPlayerOptionEntity, SwitchEntity):
    entity_description: Incomplete
    def __init__(self, mass: MusicAssistantClient, player_id: str, player_option: PlayerOption, entity_description: SwitchEntityDescription) -> None: ...
    @catch_musicassistant_error
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @catch_musicassistant_error
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def on_player_option_update(self, player_option: PlayerOption) -> None: ...
