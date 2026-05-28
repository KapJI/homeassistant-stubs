from . import MarantzIrConfigEntry as MarantzIrConfigEntry
from .const import CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, MODELS as MODELS
from .entity import MarantzIrEntity as MarantzIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData, RestoreEntity as RestoreEntity
from infrared_protocols.codes.marantz.audio import MarantzAudioCode
from typing import Any

PARALLEL_UPDATES: int
SOURCE_TO_CODE: dict[str, MarantzAudioCode]

@dataclass
class _MarantzAmplifierExtraData(ExtraStoredData):
    source: str | None
    is_volume_muted: bool | None
    def as_dict(self) -> dict[str, Any]: ...

async def async_setup_entry(hass: HomeAssistant, entry: MarantzIrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MarantzIrAmplifierMediaPlayer(MarantzIrEntity, MediaPlayerEntity, RestoreEntity):
    _attr_name: Incomplete
    _attr_assumed_state: bool
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _source_to_code: Incomplete
    _attr_source_list: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, entry: MarantzIrConfigEntry, infrared_entity_id: str) -> None: ...
    @property
    def extra_restore_state_data(self) -> ExtraStoredData: ...
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_is_volume_muted: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
