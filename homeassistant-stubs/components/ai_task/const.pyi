from . import AITaskPreferences as AITaskPreferences
from .entity import AITaskEntity as AITaskEntity
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.components.media_source import local_source as local_source
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[AITaskEntity]]
DATA_PREFERENCES: HassKey[AITaskPreferences]
DATA_MEDIA_SOURCE: HassKey[local_source.LocalSource]
IMAGE_DIR: Final[str]
IMAGE_EXPIRY_TIME: Incomplete
SERVICE_GENERATE_DATA: str
SERVICE_GENERATE_IMAGE: str
ATTR_INSTRUCTIONS: Final[str]
ATTR_TASK_NAME: Final[str]
ATTR_STRUCTURE: Final[str]
ATTR_REQUIRED: Final[str]
ATTR_ATTACHMENTS: Final[str]
DEFAULT_SYSTEM_PROMPT: str

class AITaskEntityFeature(IntFlag):
    GENERATE_DATA = 1
    SUPPORT_ATTACHMENTS = 2
    GENERATE_IMAGE = 4
