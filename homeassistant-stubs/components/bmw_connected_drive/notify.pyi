from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LOCATION as ATTR_LOCATION, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_LAT: str
ATTR_LOCATION_ATTRIBUTES: Any
ATTR_LON: str
ATTR_SUBJECT: str
ATTR_TEXT: str
_LOGGER: Any

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> BMWNotificationService: ...

class BMWNotificationService(BaseNotificationService):
    targets: Any
    def __init__(self) -> None: ...
    def setup(self, accounts: list[BMWConnectedDriveAccount]) -> None: ...
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...
