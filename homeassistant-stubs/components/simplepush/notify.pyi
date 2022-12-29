from .const import ATTR_EVENT as ATTR_EVENT, CONF_DEVICE_KEY as CONF_DEVICE_KEY, CONF_SALT as CONF_SALT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as BASE_PLATFORM_SCHEMA
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PLATFORM_SCHEMA = BASE_PLATFORM_SCHEMA
_LOGGER: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[SimplePushNotificationService, None]: ...

class SimplePushNotificationService(BaseNotificationService):
    _device_key: Incomplete
    _event: Incomplete
    _password: Incomplete
    _salt: Incomplete
    def __init__(self, config: dict[str, Any]) -> None: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
