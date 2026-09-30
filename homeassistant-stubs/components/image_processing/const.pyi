from . import ImageProcessingEntity as ImageProcessingEntity
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
SERVICE_SCAN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[ImageProcessingEntity]]

class ImageProcessingEntityStateAttribute(StrEnum):
    FACES = 'faces'
    TOTAL_FACES = 'total_faces'

class ImageProcessingDeviceClass(StrEnum):
    ALPR = 'alpr'
    FACE = 'face'
    OCR = 'ocr'
