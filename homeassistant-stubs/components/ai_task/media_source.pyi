from .const import DATA_MEDIA_SOURCE as DATA_MEDIA_SOURCE, DOMAIN as DOMAIN, IMAGE_DIR as IMAGE_DIR
from homeassistant.components.media_source import MediaSource as MediaSource, local_source as local_source
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...
