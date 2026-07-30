from .models import MediaSource as MediaSource
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaClass as MediaClass
from homeassistant.helpers.integration_platform import LazyIntegrationPlatforms as LazyIntegrationPlatforms
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_LOCAL_SOURCE: HassKey[MediaSource]
DATA_MEDIA_SOURCE_PLATFORMS: HassKey[LazyIntegrationPlatforms[MediaSource]]
MEDIA_MIME_TYPES: Incomplete
MEDIA_CLASS_MAP: Incomplete
URI_SCHEME: str
URI_SCHEME_REGEX: Incomplete
