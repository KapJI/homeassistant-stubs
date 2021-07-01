from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform, async_start_setup as async_start_setup
from homeassistant.util import slugify as slugify
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any

_LOGGER: Any
ATTR_DATA: str
ATTR_MESSAGE: str
ATTR_TARGET: str
ATTR_TITLE: str
ATTR_TITLE_DEFAULT: str
DOMAIN: str
SERVICE_NOTIFY: str
SERVICE_PERSISTENT_NOTIFICATION: str
NOTIFY_SERVICES: str
CONF_FIELDS: str
PLATFORM_SCHEMA: Any
NOTIFY_SERVICE_SCHEMA: Any
PERSISTENT_NOTIFICATION_SERVICE_SCHEMA: Any

async def async_reload(hass: HomeAssistant, integration_name: str) -> None: ...
async def async_reset_platform(hass: HomeAssistant, integration_name: str) -> None: ...
def _async_integration_has_notify_services(hass: HomeAssistant, integration_name: str) -> bool: ...

class BaseNotificationService:
    hass: HomeAssistant
    registered_targets: dict[str, str]
    def send_message(self, message, **kwargs) -> None: ...
    async def async_send_message(self, message: Any, **kwargs: Any) -> None: ...
    async def _async_notify_message_service(self, service: ServiceCall) -> None: ...
    _service_name: Any
    _target_service_name_prefix: Any
    services_dict: Any
    async def async_setup(self, hass: HomeAssistant, service_name: str, target_service_name_prefix: str) -> None: ...
    async def async_register_services(self) -> None: ...
    async def async_unregister_services(self) -> None: ...

async def async_setup(hass, config): ...
