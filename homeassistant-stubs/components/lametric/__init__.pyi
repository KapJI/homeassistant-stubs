from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class HassLaMetricManager:
    manager: Incomplete
    _client_id: Incomplete
    _client_secret: Incomplete
    def __init__(self, client_id: str, client_secret: str) -> None: ...
