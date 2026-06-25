from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, DOMAIN as DOMAIN, SamsungDeviceType as SamsungDeviceType
from .entity import SamsungIrEntity as SamsungIrEntity
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.samsung.tv import SamsungTVCode
from typing import override

PARALLEL_UPDATES: int
SOURCE_MAP: dict[str, SamsungTVCode]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SamsungIrTvMediaPlayer(SamsungIrEntity, InfraredEmitterConsumerEntity, MediaPlayerEntity):
    _attr_name: Incomplete
    _attr_assumed_state: bool
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_source_list: Incomplete
    _attr_source: Incomplete
    _attr_state: Incomplete
    _attr_translation_key: str
    _infrared_emitter_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, infrared_emitter_entity_id: str) -> None: ...
    @override
    async def async_turn_on(self) -> None: ...
    @override
    async def async_turn_off(self) -> None: ...
    @override
    async def async_volume_up(self) -> None: ...
    @override
    async def async_volume_down(self) -> None: ...
    @override
    async def async_mute_volume(self, mute: bool) -> None: ...
    @override
    async def async_media_next_track(self) -> None: ...
    @override
    async def async_media_previous_track(self) -> None: ...
    @override
    async def async_media_play(self) -> None: ...
    @override
    async def async_media_pause(self) -> None: ...
    @override
    async def async_media_stop(self) -> None: ...
    @override
    async def async_select_source(self, source: str) -> None: ...
