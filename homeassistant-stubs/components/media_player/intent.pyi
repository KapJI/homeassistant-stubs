from . import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, DOMAIN as DOMAIN, MediaPlayerDeviceClass as MediaPlayerDeviceClass, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SEARCH_MEDIA as SERVICE_SEARCH_MEDIA, SearchMedia as SearchMedia
from .const import ATTR_MEDIA_FILTER_CLASSES as ATTR_MEDIA_FILTER_CLASSES, MediaClass as MediaClass, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass, field
from homeassistant.const import SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PREVIOUS_TRACK as SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import intent as intent

INTENT_MEDIA_PAUSE: str
INTENT_MEDIA_UNPAUSE: str
INTENT_MEDIA_NEXT: str
INTENT_MEDIA_PREVIOUS: str
INTENT_SET_VOLUME: str
INTENT_MEDIA_SEARCH_AND_PLAY: str
_LOGGER: Incomplete

@dataclass
class LastPaused:
    timestamp: float | None = ...
    context: Context | None = ...
    entity_ids: set[str] = field(default_factory=set)
    def clear(self) -> None: ...
    def update(self, context: Context | None, entity_ids: Iterable[str]) -> None: ...
    def __bool__(self) -> bool: ...

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class MediaPauseHandler(intent.ServiceIntentHandler):
    last_paused: Incomplete
    def __init__(self, last_paused: LastPaused) -> None: ...
    async def async_handle_states(self, intent_obj: intent.Intent, match_result: intent.MatchTargetsResult, match_constraints: intent.MatchTargetsConstraints, match_preferences: intent.MatchTargetsPreferences | None = None) -> intent.IntentResponse: ...

class MediaUnpauseHandler(intent.ServiceIntentHandler):
    last_paused: Incomplete
    def __init__(self, last_paused: LastPaused) -> None: ...
    async def async_handle_states(self, intent_obj: intent.Intent, match_result: intent.MatchTargetsResult, match_constraints: intent.MatchTargetsConstraints, match_preferences: intent.MatchTargetsPreferences | None = None) -> intent.IntentResponse: ...

class MediaSearchAndPlayHandler(intent.IntentHandler):
    description: str
    intent_type = INTENT_MEDIA_SEARCH_AND_PLAY
    slot_schema: Incomplete
    platforms: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
