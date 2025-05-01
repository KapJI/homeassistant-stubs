from . import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow

class OncueConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
