from . import DOMAIN as DOMAIN, HassLaMetricManager as HassLaMetricManager
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_ICON as CONF_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
AVAILABLE_PRIORITIES: Any
AVAILABLE_ICON_TYPES: Any
CONF_CYCLES: str
CONF_LIFETIME: str
CONF_PRIORITY: str
CONF_ICON_TYPE: str

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> LaMetricNotificationService: ...

class LaMetricNotificationService(BaseNotificationService):
    hasslametricmanager: Any
    _icon: Any
    _lifetime: Any
    _cycles: Any
    _priority: Any
    _icon_type: Any
    _devices: Any
    def __init__(self, hasslametricmanager: HassLaMetricManager, icon: str, lifetime: int, cycles: int, priority: str, icon_type: str) -> None: ...
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...
