from . import ImageEntity as ImageEntity
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

class ImageEntityStateAttribute(StrEnum):
    ACCESS_TOKEN = 'access_token'

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[ImageEntity]]
IMAGE_TIMEOUT: Final[int]
