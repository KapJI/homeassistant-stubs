from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONFIG_SCHEMA: Any

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HassLaMetricManager:
    manager: Any
    _client_id: Any
    _client_secret: Any
    def __init__(self, client_id: str, client_secret: str) -> None: ...
