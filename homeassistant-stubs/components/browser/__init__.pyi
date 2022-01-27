from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ATTR_URL: str
ATTR_URL_DEFAULT: str
DOMAIN: str
SERVICE_BROWSE_URL: str
SERVICE_BROWSE_URL_SCHEMA: Any

def _browser_url(service: ServiceCall) -> None: ...
def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
