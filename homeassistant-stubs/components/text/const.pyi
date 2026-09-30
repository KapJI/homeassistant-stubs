from . import TextEntity as TextEntity
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[TextEntity]]

class TextEntityCapabilityAttribute(StrEnum):
    MODE = 'mode'
    MIN = 'min'
    MAX = 'max'
    PATTERN = 'pattern'

ATTR_MAX: str
ATTR_MIN: str
ATTR_PATTERN: str
ATTR_VALUE: str
SERVICE_SET_VALUE: str
