from _typeshed import Incomplete
from enum import StrEnum

DOMAIN: str
LOGGER: Incomplete
AUTHORIZE_URL: str
TOKEN_URL: str
CLIENT_ID: str
SUBENTRY_TYPE_VEHICLE: str
CONF_VIN: str
VEHICLE_KEY_FILE: str
BLE_PARENT_KEY: Incomplete
BLE_PARENT_LOCK_KEY: Incomplete
BLE_DISCONNECT_TIMEOUT: int
SUBENTRY_TYPE_ENERGY_SITE: str
CONF_SITE_ID: str
POWERWALL_KEY_FILE: str
RSA_PARENT_KEY: Incomplete
ISSUE_GATEWAY_NOT_FOUND: str
ENERGY_HISTORY_FIELDS: Incomplete
VEHICLE_ISSUE_LEARN_MORE: dict[str, str | None]

class TeslemetryState(StrEnum):
    ONLINE = 'online'
    ASLEEP = 'asleep'
    OFFLINE = 'offline'

class TeslemetryClimateSide(StrEnum):
    DRIVER = 'driver_temp'
    PASSENGER = 'passenger_temp'
