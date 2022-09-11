from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LOCATION as ATTR_LOCATION, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_LAT: str
ATTR_LOCATION_ATTRIBUTES: Incomplete
ATTR_LON: str
ATTR_SUBJECT: str
ATTR_TEXT: str
_LOGGER: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> BMWNotificationService: ...

class BMWNotificationService(BaseNotificationService):
    targets: Incomplete
    def __init__(self, targets: dict[str, MyBMWVehicle]) -> None: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...
