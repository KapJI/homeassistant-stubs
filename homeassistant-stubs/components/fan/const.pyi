from . import FanEntity as FanEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[FanEntity]]
SERVICE_INCREASE_SPEED: str
SERVICE_DECREASE_SPEED: str
SERVICE_OSCILLATE: str
SERVICE_SET_DIRECTION: str
SERVICE_SET_PERCENTAGE: str
SERVICE_SET_PRESET_MODE: str
DIRECTION_FORWARD: str
DIRECTION_REVERSE: str
ATTR_PERCENTAGE: str
ATTR_PERCENTAGE_STEP: str
ATTR_OSCILLATING: str
ATTR_DIRECTION: str
ATTR_PRESET_MODE: str
ATTR_PRESET_MODES: str

class FanEntityCapabilityAttribute(StrEnum):
    PRESET_MODES = 'preset_modes'

class FanEntityStateAttribute(StrEnum):
    DIRECTION = 'direction'
    OSCILLATING = 'oscillating'
    PERCENTAGE = 'percentage'
    PERCENTAGE_STEP = 'percentage_step'
    PRESET_MODE = 'preset_mode'

class FanEntityFeature(IntFlag):
    SET_SPEED = 1
    OSCILLATE = 2
    DIRECTION = 4
    PRESET_MODE = 8
    TURN_OFF = 16
    TURN_ON = 32
