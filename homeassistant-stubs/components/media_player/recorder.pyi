from . import ATTR_ENTITY_PICTURE_LOCAL as ATTR_ENTITY_PICTURE_LOCAL, ATTR_INPUT_SOURCE_LIST as ATTR_INPUT_SOURCE_LIST, ATTR_MEDIA_POSITION as ATTR_MEDIA_POSITION, ATTR_MEDIA_POSITION_UPDATED_AT as ATTR_MEDIA_POSITION_UPDATED_AT, ATTR_SOUND_MODE_LIST as ATTR_SOUND_MODE_LIST
from homeassistant.const import ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
