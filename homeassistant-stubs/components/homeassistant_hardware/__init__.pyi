from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from .helpers import HardwareInfoDispatcher as HardwareInfoDispatcher
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
