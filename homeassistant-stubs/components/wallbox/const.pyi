from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum

DOMAIN: str
BIDIRECTIONAL_MODEL_PREFIXES: Incomplete
CONF_STATION: str
CHARGER_ADDED_DISCHARGED_ENERGY_KEY: str
CHARGER_ADDED_ENERGY_KEY: str
CHARGER_ADDED_RANGE_KEY: str
CHARGER_CHARGING_POWER_KEY: str
CHARGER_CHARGING_SPEED_KEY: str
CHARGER_CHARGING_TIME_KEY: str
CHARGER_COST_KEY: str
CHARGER_CURRENT_MODE_KEY: str
CHARGER_CURRENT_VERSION_KEY: str
CHARGER_DATA_KEY: str
CHARGER_DEPOT_PRICE_KEY: str
CHARGER_SERIAL_NUMBER_KEY: str
CHARGER_PART_NUMBER_KEY: str
CHARGER_SOFTWARE_KEY: str
CHARGER_MAX_AVAILABLE_POWER_KEY: str
CHARGER_MAX_CHARGING_CURRENT_KEY: str
CHARGER_PAUSE_RESUME_KEY: str
CHARGER_LOCKED_UNLOCKED_KEY: str
CHARGER_NAME_KEY: str
CHARGER_STATE_OF_CHARGE_KEY: str
CHARGER_STATUS_ID_KEY: str
CHARGER_STATUS_DESCRIPTION_KEY: str
CHARGER_CONNECTIONS: str

class ChargerStatus(StrEnum):
    CHARGING: str
    DISCHARGING: str
    PAUSED: str
    SCHEDULED: str
    WAITING_FOR_CAR: str
    WAITING: str
    DISCONNECTED: str
    ERROR: str
    READY: str
    LOCKED: str
    LOCKED_CAR_CONNECTED: str
    UPDATING: str
    WAITING_IN_QUEUE_POWER_SHARING: str
    WAITING_IN_QUEUE_POWER_BOOST: str
    WAITING_MID_FAILED: str
    WAITING_MID_SAFETY: str
    WAITING_IN_QUEUE_ECO_SMART: str
    UNKNOWN: str
