from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename, raise_if_invalid_path as raise_if_invalid_path

_LOGGER: Incomplete
ATTR_FILENAME: str
ATTR_SUBDIR: str
ATTR_URL: str
ATTR_OVERWRITE: str
CONF_DOWNLOAD_DIR: str
DOMAIN: str
DOWNLOAD_FAILED_EVENT: str
DOWNLOAD_COMPLETED_EVENT: str
SERVICE_DOWNLOAD_FILE: str
SERVICE_DOWNLOAD_FILE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
