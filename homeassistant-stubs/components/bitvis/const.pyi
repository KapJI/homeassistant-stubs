from .coordinator import BitvisListenerRegistry as BitvisListenerRegistry
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
MANUFACTURER: str
MODEL_NAME: str
DEFAULT_NAME: str
DEFAULT_PORT: int
DISCOVERY_TIMEOUT: int
DATA_LISTENER_REGISTRY: HassKey[BitvisListenerRegistry]
