from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform
from homeassistant.util import slugify as slugify
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any, Dict, Optional

ATTR_DATA: str
ATTR_MESSAGE: str
ATTR_TARGET: str
ATTR_TITLE: str
ATTR_TITLE_DEFAULT: str
DOMAIN: str
SERVICE_NOTIFY: str
SERVICE_PERSISTENT_NOTIFICATION: str
NOTIFY_SERVICES: str
CONF_DESCRIPTION: str
CONF_FIELDS: str
PLATFORM_SCHEMA: Any
NOTIFY_SERVICE_SCHEMA: Any
PERSISTENT_NOTIFICATION_SERVICE_SCHEMA: Any

async def async_reload(hass: HomeAssistantType, integration_name: str) -> None: ...
async def async_reset_platform(hass: HomeAssistantType, integration_name: str) -> None: ...

class BaseNotificationService:
    hass: Optional[HomeAssistantType] = ...
    registered_targets: Dict[str, str]
    def send_message(self, message: Any, **kwargs: Any) -> None: ...
    async def async_send_message(self, message: Any, **kwargs: Any) -> None: ...
    services_dict: Any = ...
    async def async_setup(self, hass: HomeAssistantType, service_name: str, target_service_name_prefix: str) -> None: ...
    async def async_register_services(self) -> None: ...
    async def async_unregister_services(self) -> None: ...

async def async_setup(hass: Any, config: Any): ...
