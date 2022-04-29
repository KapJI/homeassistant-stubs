import logging
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from pyoverkiz.enums import UIClass, UIWidget
from typing import Final

DOMAIN: Final[str]
LOGGER: logging.Logger
CONF_HUB: Final[str]
DEFAULT_HUB: Final[str]
UPDATE_INTERVAL: Final[Incomplete]
UPDATE_INTERVAL_ALL_ASSUMED_STATE: Final[Incomplete]
PLATFORMS: list[Platform]
IGNORED_OVERKIZ_DEVICES: list[Union[UIClass, UIWidget]]
OVERKIZ_DEVICE_TO_PLATFORM: dict[Union[UIClass, UIWidget], Union[Platform, None]]
OVERKIZ_STATE_TO_TRANSLATION: dict[str, str]
