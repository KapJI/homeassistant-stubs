from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_HEADERS as CONF_HEADERS, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PARAMS as CONF_PARAMS, CONF_PASSWORD as CONF_PASSWORD, CONF_RESOURCE as CONF_RESOURCE, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from requests.auth import AuthBase
from typing import Any

CONF_DATA: str
CONF_DATA_TEMPLATE: str
CONF_MESSAGE_PARAMETER_NAME: str
CONF_TARGET_PARAMETER_NAME: str
CONF_TITLE_PARAMETER_NAME: str
DEFAULT_MESSAGE_PARAM_NAME: str
DEFAULT_METHOD: str
DEFAULT_VERIFY_SSL: bool
_LOGGER: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> RestNotificationService: ...

class RestNotificationService(BaseNotificationService):
    _resource: Incomplete
    _hass: Incomplete
    _method: Incomplete
    _headers: Incomplete
    _params: Incomplete
    _message_param_name: Incomplete
    _title_param_name: Incomplete
    _target_param_name: Incomplete
    _data: Incomplete
    _data_template: Incomplete
    _auth: Incomplete
    _verify_ssl: Incomplete
    def __init__(self, hass: HomeAssistant, resource: str, method: str, headers: Union[dict[str, str], None], params: Union[dict[str, str], None], message_param_name: str, title_param_name: Union[str, None], target_param_name: Union[str, None], data: Union[dict[str, Any], None], data_template: Union[dict[str, Any], None], auth: Union[AuthBase, None], verify_ssl: bool) -> None: ...
    def send_message(self, message: str = ..., **kwargs: Any) -> None: ...
