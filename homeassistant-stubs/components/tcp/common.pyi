import voluptuous as vol
from .const import CONF_BUFFER_SIZE as CONF_BUFFER_SIZE, CONF_VALUE_ON as CONF_VALUE_ON, DEFAULT_BUFFER_SIZE as DEFAULT_BUFFER_SIZE, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL
from .model import TcpSensorConfig as TcpSensorConfig
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

_LOGGER: Final[Incomplete]
TCP_PLATFORM_SCHEMA: Final[dict[vol.Marker, Any]]

class TcpEntity(Entity):
    _hass: Incomplete
    _config: Incomplete
    _ssl_context: Incomplete
    _state: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @property
    def name(self) -> str: ...
    def update(self) -> None: ...
