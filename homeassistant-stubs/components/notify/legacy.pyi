from .const import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, DOMAIN as DOMAIN, LOGGER as LOGGER, NOTIFY_SERVICE_SCHEMA as NOTIFY_SERVICE_SCHEMA, SERVICE_NOTIFY as SERVICE_NOTIFY
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, discovery as discovery, template as template
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from homeassistant.setup import async_prepare_setup_platform as async_prepare_setup_platform, async_start_setup as async_start_setup
from homeassistant.util import slugify as slugify
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any, Protocol

CONF_FIELDS: str
NOTIFY_SERVICES: str
NOTIFY_DISCOVERY_DISPATCHER: str

class LegacyNotifyPlatform(Protocol):
    async def async_get_service(self, hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> BaseNotificationService: ...
    def get_service(self, hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> BaseNotificationService: ...

def async_setup_legacy(hass: HomeAssistant, config: ConfigType) -> list[Coroutine[Any, Any, None]]: ...
def check_templates_warn(hass: HomeAssistant, tpl: template.Template) -> None: ...
async def async_reload(hass: HomeAssistant, integration_name: str) -> None: ...
async def async_reset_platform(hass: HomeAssistant, integration_name: str) -> None: ...
def _async_integration_has_notify_services(hass: HomeAssistant, integration_name: str) -> bool: ...

class BaseNotificationService:
    hass: HomeAssistant
    registered_targets: dict[str, str]
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    async def async_send_message(self, message: str, **kwargs: Any) -> None: ...
    async def _async_notify_message_service(self, service: ServiceCall) -> None: ...
    _service_name: Incomplete
    _target_service_name_prefix: Incomplete
    services_dict: Incomplete
    async def async_setup(self, hass: HomeAssistant, service_name: str, target_service_name_prefix: str) -> None: ...
    async def async_register_services(self) -> None: ...
    async def async_unregister_services(self) -> None: ...
