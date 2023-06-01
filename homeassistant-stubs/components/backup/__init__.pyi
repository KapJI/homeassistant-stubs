from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .http import async_register_http_views as async_register_http_views
from .manager import BackupManager as BackupManager
from .websocket import async_register_websocket_handlers as async_register_websocket_handlers
from _typeshed import Incomplete
from homeassistant.components.hassio import is_hassio as is_hassio
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
