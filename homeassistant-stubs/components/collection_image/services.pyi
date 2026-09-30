from .const import DOMAIN as DOMAIN
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.selector import MediaSelector as MediaSelector

class CollectionImageService(StrEnum):
    SHUFFLE = 'shuffle'
    SELECT_FIRST = 'select_first'
    SELECT_LAST = 'select_last'
    SELECT_NEXT = 'select_next'
    SELECT_PREVIOUS = 'select_previous'
    SELECT_IMAGE = 'select_image'

class CollectionImageServiceArgument(StrEnum):
    WRAP = 'wrap'
    IMAGE = 'image'

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
