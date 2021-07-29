from . import util as util
from .const import ATTR_ADAPTERS as ATTR_ADAPTERS, ATTR_CONFIGURED_ADAPTERS as ATTR_CONFIGURED_ADAPTERS, DOMAIN as DOMAIN, NETWORK_CONFIG_SCHEMA as NETWORK_CONFIG_SCHEMA
from .models import Adapter as Adapter
from .network import Network as Network
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

ZEROCONF_DOMAIN: str
_LOGGER: Any

async def async_get_adapters(hass: HomeAssistant) -> list[Adapter]: ...
async def async_get_source_ip(hass: HomeAssistant, target_ip: str) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def websocket_network_adapters(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def websocket_network_adapters_configure(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
