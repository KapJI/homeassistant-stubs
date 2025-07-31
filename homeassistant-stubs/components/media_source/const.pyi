from .models import MediaSource as MediaSource
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaClass as MediaClass
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
MEDIA_SOURCE_DATA: HassKey[dict[str, MediaSource]]
MEDIA_MIME_TYPES: Incomplete
MEDIA_CLASS_MAP: Incomplete
URI_SCHEME: str
URI_SCHEME_REGEX: Incomplete
