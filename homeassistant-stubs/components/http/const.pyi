from enum import StrEnum
from homeassistant.helpers.http import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS
from typing import Final

DOMAIN: Final[str]
KEY_HASS_USER: Final[str]
KEY_HASS_REFRESH_TOKEN_ID: Final[str]

class StrictConnectionMode(StrEnum):
    DISABLED: str
    GUARD_PAGE: str
    DROP_CONNECTION: str
