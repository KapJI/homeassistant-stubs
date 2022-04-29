from .const import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, DOMAIN as DOMAIN, NOTIFY_SERVICE_SCHEMA as NOTIFY_SERVICE_SCHEMA, PERSISTENT_NOTIFICATION_SERVICE_SCHEMA as PERSISTENT_NOTIFICATION_SERVICE_SCHEMA, SERVICE_NOTIFY as SERVICE_NOTIFY, SERVICE_PERSISTENT_NOTIFICATION as SERVICE_PERSISTENT_NOTIFICATION
from .legacy import BaseNotificationService as BaseNotificationService, async_reload as async_reload, async_reset_platform as async_reset_platform, async_setup_legacy as async_setup_legacy, check_templates_warn as check_templates_warn
from _typeshed import Incomplete
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType

ATTR_TITLE_DEFAULT: str
PLATFORM_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
