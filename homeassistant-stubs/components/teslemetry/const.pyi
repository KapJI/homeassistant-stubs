from _typeshed import Incomplete
from enum import StrEnum

DOMAIN: str
LOGGER: Incomplete
AUTHORIZE_URL: str
TOKEN_URL: str
CLIENT_ID: str
ENERGY_HISTORY_FIELDS: Incomplete

class TeslemetryState(StrEnum):
    ONLINE = 'online'
    ASLEEP = 'asleep'
    OFFLINE = 'offline'

class TeslemetryClimateSide(StrEnum):
    DRIVER = 'driver_temp'
    PASSENGER = 'passenger_temp'
