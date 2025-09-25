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

class ProgramPhaseWashingMachine(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    pre_wash: Incomplete
    soak: int
    main_wash: int
    rinse: int
    rinse_hold: int
    cleaning: int
    cooling_down: int
    drain: int
    spin: int
    anti_crease: int
    finished: int
    venting: int
    starch_stop: int
    freshen_up_and_moisten: int
    steam_smoothing: Incomplete
    hygiene: int
    drying: int
    disinfecting: int

class ProgramPhaseTumbleDryer(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    program_running: int
    drying: int
    machine_iron: int
    hand_iron_2: int
    normal: int
    normal_plus: int
    cooling_down: int
    hand_iron_1: int
    anti_crease: int
    finished: int
    extra_dry: int
    hand_iron: int
    moisten: int
    thermo_spin: int
    timed_drying: int
    warm_air: int
    steam_smoothing: int
    comfort_cooling: int
    rinse_out_lint: int
    rinses: int
    smoothing: int
    slightly_dry: int
    safety_cooling: int

class ProgramPhaseWasherDryer(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    pre_wash: Incomplete
    soak: int
    main_wash: int
    rinse: int
    rinse_hold: int
    cleaning: int
    cooling_down: Incomplete
    drain: int
    spin: int
    anti_crease: Incomplete
    finished: Incomplete
    venting: int
    starch_stop: int
    freshen_up_and_moisten: int
    steam_smoothing: Incomplete
    hygiene: int
    drying: Incomplete
    disinfecting: int
    program_running: int
    machine_iron: int
    hand_iron_2: int
    normal: int
    normal_plus: int
    hand_iron_1: int
    extra_dry: int
    hand_iron: int
    moisten: int
    thermo_spin: int
    timed_drying: int
    warm_air: int
    comfort_cooling: int
    rinse_out_lint: int
    rinses: int
    smoothing: int
    slightly_dry: int
    safety_cooling: int

class ProgramPhaseDishwasher(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    reactivating: int
    pre_dishwash: Incomplete
    main_dishwash: int
    rinse: int
    interim_rinse: int
    final_rinse: int
    drying: int
    finished: int

class ProgramPhaseOven(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating_up: int
    process_running: int
    process_finished: int
    energy_save: int
    pre_heating: int

class ProgramPhaseWarmingDrawer(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating_up: int
    door_open: int
    keeping_warm: int
    cooling_down: int

class ProgramPhaseMicrowave(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating: int
    process_running: int
    process_finished: int
    energy_save: int

class ProgramPhaseCoffeeSystem(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating_up: int
    espresso: int
    hot_milk: int
    milk_foam: int
    dispensing: Incomplete
    pre_brewing: int
    grinding: int
    second_espresso: int
    second_pre_brewing: int
    second_grinding: int
    rinse: int

class ProgramPhaseRobotVacuumCleaner(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    vacuum_cleaning: int
    returning: int
    vacuum_cleaning_paused: int
    going_to_target_area: int
    wheel_lifted: int
    dirty_sensors: int
    dust_box_missing: int
    blocked_drive_wheels: int
    blocked_brushes: int
    motor_overload: int
    internal_fault: int
    blocked_front_wheel: int
    docked: Incomplete
    remote_controlled: int

class ProgramPhaseMicrowaveOvenCombo(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    steam_reduction: int
    process_running: int
    waiting_for_start: int
    heating_up_phase: int
    process_finished: int

class ProgramPhaseSteamOven(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    steam_reduction: int
    process_running: int
    waiting_for_start: int
    heating_up_phase: int
    process_finished: int

class ProgramPhaseSteamOvenCombi(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating_up: int
    process_running: Incomplete
    process_finished: Incomplete
    energy_save: int
    pre_heating: int
    steam_reduction: int
    waiting_for_start: int
    heating_up_phase: int

class ProgramPhaseSteamOvenMicro(MieleEnum, missing_to_none=True):
    not_running: Incomplete
    heating: int
    process_running: Incomplete
    process_finished: int
    energy_save: int
    steam_reduction: int
    waiting_for_start: int
    heating_up_phase: int

PROGRAM_PHASE: dict[int, type[MieleEnum]]

class StateProgramType(MieleEnum, missing_to_none=True):
    normal_operation_mode: int
    own_program: int
    automatic_program: int
    cleaning_care_program: int
    maintenance_program: int

class StateDryingStep(MieleEnum, missing_to_none=True):
    extra_dry: int
    normal_plus: int
    normal: int
    slightly_dry: int
    hand_iron_1: int
    hand_iron_2: int
    machine_iron: int
    smoothing: int

WASHING_MACHINE_PROGRAM_ID: dict[int, str]
DISHWASHER_PROGRAM_ID: dict[int, str]
TUMBLE_DRYER_PROGRAM_ID: dict[int, str]
OVEN_PROGRAM_ID: dict[int, str]
DISH_WARMER_PROGRAM_ID: dict[int, str]
ROBOT_VACUUM_CLEANER_PROGRAM_ID: dict[int, str]
COFFEE_SYSTEM_PROGRAM_ID: dict[int, str]
COFFEE_SYSTEM_PROFILE: dict[range, str]
STEAM_OVEN_MICRO_PROGRAM_ID: dict[int, str]
STATE_PROGRAM_ID: dict[int, dict[int, str]]

class PlatePowerStep(MieleEnum, missing_to_none=True):
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
    plate_step_boost_2: int
