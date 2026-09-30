from . import WaterHeaterEntity as WaterHeaterEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.deprecation import EnumWithDeprecatedMembers as EnumWithDeprecatedMembers
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
ATTR_AWAY_MODE: Final[str]
ATTR_OPERATION_MODE: Final[str]
SERVICE_SET_AWAY_MODE: Final[str]
SERVICE_SET_OPERATION_MODE: Final[str]
SERVICE_SET_TEMPERATURE: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[WaterHeaterEntity]]

class WaterHeaterCapabilityAttribute(StrEnum):
    MIN_TEMP = 'min_temp'
    MAX_TEMP = 'max_temp'
    TARGET_TEMP_STEP = 'target_temp_step'
    OPERATION_LIST = 'operation_list'

class WaterHeaterStateAttribute(StrEnum, deprecated={'TEMPERATURE': ('ClimateEntityStateAttribute.TARGET_TEMPERATURE', '2027.3.0')}, metaclass=EnumWithDeprecatedMembers):
    CURRENT_TEMPERATURE = 'current_temperature'
    TARGET_TEMPERATURE = 'temperature'
    TEMPERATURE = 'temperature'
    TARGET_TEMP_HIGH = 'target_temp_high'
    TARGET_TEMP_LOW = 'target_temp_low'
    OPERATION_MODE = 'operation_mode'
    AWAY_MODE = 'away_mode'

STATE_ECO: str
STATE_ELECTRIC: str
STATE_PERFORMANCE: str
STATE_HIGH_DEMAND: str
STATE_HEAT_PUMP: str
STATE_GAS: str

class WaterHeaterEntityFeature(IntFlag):
    TARGET_TEMPERATURE = 1
    OPERATION_MODE = 2
    AWAY_MODE = 4
    ON_OFF = 8
