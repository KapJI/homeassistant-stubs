from .discovery import ZeroconfDiscovery as ZeroconfDiscovery
from .models import HaAsyncZeroconf as HaAsyncZeroconf
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
ZEROCONF_TYPE: str
REQUEST_TIMEOUT: int
DATA_INSTANCE: HassKey[HaAsyncZeroconf]
DATA_DISCOVERY: HassKey[ZeroconfDiscovery]
