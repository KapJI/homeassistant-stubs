from .const import DOMAIN as DOMAIN, PING_PRIVS as PING_PRIVS, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _can_use_icmp_lib_with_privilege() -> None | bool: ...
