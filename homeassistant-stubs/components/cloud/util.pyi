from .client import CloudClient as CloudClient
from .const import DOMAIN as DOMAIN
from hass_nabucasa import Cloud as Cloud
from homeassistant.components import http as http
from homeassistant.core import HomeAssistant as HomeAssistant

def get_strict_connection_mode(hass: HomeAssistant) -> http.const.StrictConnectionMode: ...
