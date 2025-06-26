from _typeshed import Incomplete
from enum import IntEnum
from pymiele import MieleEnum

DOMAIN: str
MANUFACTURER: str
ACTIONS: str
POWER_ON: str
POWER_OFF: str
PROCESS_ACTION: str
PROGRAM_ID: str
VENTILATION_STEP: str
TARGET_TEMPERATURE: str
AMBIENT_LIGHT: str
LIGHT: str
LIGHT_ON: int
LIGHT_OFF: int
DISABLED_TEMP_ENTITIES: Incomplete

class MieleAppliance(IntEnum):
    WASHING_MACHINE = 1
    TUMBLE_DRYER = 2
    WASHING_MACHINE_SEMI_PROFESSIONAL = 3
    TUMBLE_DRYER_SEMI_PROFESSIONAL = 4
    WASHING_MACHINE_PROFESSIONAL = 5
    DRYER_PROFESSIONAL = 6
    DISHWASHER = 7
    DISHWASHER_SEMI_PROFESSIONAL = 8
    DISHWASHER_PROFESSIONAL = 9
    OVEN = 12
    OVEN_MICROWAVE = 13
    HOB_HIGHLIGHT = 14
    STEAM_OVEN = 15
    MICROWAVE = 16
    COFFEE_SYSTEM = 17
    HOOD = 18
    FRIDGE = 19
    FREEZER = 20
    FRIDGE_FREEZER = 21
    ROBOT_VACUUM_CLEANER = 23
    WASHER_DRYER = 24
    DISH_WARMER = 25
    HOB_INDUCTION = 27
    STEAM_OVEN_COMBI = 31
    WINE_CABINET = 32
    WINE_CONDITIONING_UNIT = 33
    WINE_STORAGE_CONDITIONING_UNIT = 34
    STEAM_OVEN_MICRO = 45
    DIALOG_OVEN = 67
    WINE_CABINET_FREEZER = 68
    STEAM_OVEN_MK2 = 73
    HOB_INDUCT_EXTR = 74

DEVICE_TYPE_TAGS: Incomplete

class StateStatus(IntEnum):
    RESERVED = 0
    OFF = 1
    ON = 2
    PROGRAMMED = 3
    WAITING_TO_START = 4
    IN_USE = 5
    PAUSE = 6
    PROGRAM_ENDED = 7
    FAILURE = 8
    PROGRAM_INTERRUPTED = 9
    IDLE = 10
    RINSE_HOLD = 11
    SERVICE = 12
    SUPERFREEZING = 13
    SUPERCOOLING = 14
    SUPERHEATING = 15
    SUPERCOOLING_SUPERFREEZING = 146
    AUTOCLEANING = 147
    NOT_CONNECTED = 255

STATE_STATUS_TAGS: Incomplete

class MieleActions(IntEnum):
    START = 1
    STOP = 2
    PAUSE = 3
    START_SUPERFREEZE = 4
    STOP_SUPERFREEZE = 5
    START_SUPERCOOL = 6
    STOP_SUPERCOOL = 7

PROCESS_ACTIONS: Incomplete
STATE_PROGRAM_PHASE_WASHING_MACHINE: Incomplete
STATE_PROGRAM_PHASE_TUMBLE_DRYER: Incomplete
STATE_PROGRAM_PHASE_DISHWASHER: Incomplete
STATE_PROGRAM_PHASE_OVEN: Incomplete
STATE_PROGRAM_PHASE_WARMING_DRAWER: Incomplete
STATE_PROGRAM_PHASE_MICROWAVE: Incomplete
STATE_PROGRAM_PHASE_COFFEE_SYSTEM: Incomplete
STATE_PROGRAM_PHASE_ROBOT_VACUUM_CLEANER: Incomplete
STATE_PROGRAM_PHASE_STEAM_OVEN: Incomplete
STATE_PROGRAM_PHASE: dict[int, dict[int, str]]

class StateProgramType(MieleEnum):
    normal_operation_mode: int
    own_program: int
    automatic_program: int
    cleaning_care_program: int
    maintenance_program: int
    missing2none: int

class StateDryingStep(MieleEnum):
    extra_dry: int
    normal_plus: int
    normal: int
    slightly_dry: int
    hand_iron_1: int
    hand_iron_2: int
    machine_iron: int
    smoothing: int
    missing2none: int

WASHING_MACHINE_PROGRAM_ID: dict[int, str]
DISHWASHER_PROGRAM_ID: dict[int, str]
TUMBLE_DRYER_PROGRAM_ID: dict[int, str]
OVEN_PROGRAM_ID: dict[int, str]
DISH_WARMER_PROGRAM_ID: dict[int, str]
ROBOT_VACUUM_CLEANER_PROGRAM_ID: dict[int, str]
COFFEE_SYSTEM_PROGRAM_ID: dict[int, str]
STEAM_OVEN_MICRO_PROGRAM_ID: dict[int, str]
STATE_PROGRAM_ID: dict[int, dict[int, str]]

class PlatePowerStep(MieleEnum):
    plate_step_0: int
    plate_step_warming: Incomplete
    plate_step_1: int
    plate_step_2: int
    plate_step_3: int
    plate_step_4: int
    plate_step_5: int
    plate_step_6: int
    plate_step_7: int
    plate_step_8: int
    plate_step_9: int
    plate_step_10: int
    plate_step_11: int
    plate_step_12: int
    plate_step_13: int
    plate_step_14: int
    plate_step_15: int
    plate_step_16: int
    plate_step_17: int
    plate_step_18: int
    plate_step_boost: Incomplete
    missing2none: int
