from enum import StrEnum

DOMAIN: str

class WaterHeaterCapabilityAttribute(StrEnum):
    MIN_TEMP = 'min_temp'
    MAX_TEMP = 'max_temp'
    TARGET_TEMP_STEP = 'target_temp_step'
    OPERATION_LIST = 'operation_list'

class WaterHeaterStateAttribute(StrEnum):
    CURRENT_TEMPERATURE = 'current_temperature'
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
