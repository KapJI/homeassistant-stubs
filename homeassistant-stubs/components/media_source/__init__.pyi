from .const import DOMAIN as DOMAIN, MEDIA_CLASS_MAP as MEDIA_CLASS_MAP, MEDIA_MIME_TYPES as MEDIA_MIME_TYPES
from .error import MediaSourceError as MediaSourceError, Unresolvable as Unresolvable
from .helper import async_browse_media as async_browse_media, async_resolve_media as async_resolve_media
from .models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from homeassistant.core import HomeAssistant
from typing import Protocol

__all__ = ['DOMAIN', 'MEDIA_CLASS_MAP', 'MEDIA_MIME_TYPES', 'BrowseMediaSource', 'MediaSource', 'MediaSourceError', 'MediaSourceItem', 'PlayMedia', 'Unresolvable', 'async_browse_media', 'async_resolve_media', 'generate_media_source_id', 'is_media_source_id']

class MediaSourceProtocol(Protocol):
    async def async_get_media_source(self, hass: HomeAssistant) -> MediaSource: ...

def is_media_source_id(media_content_id: str) -> bool: ...
def generate_media_source_id(domain: str, identifier: str) -> str: ...
