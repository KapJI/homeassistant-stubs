from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

@dataclass(slots=True)
class PingDomainData:
    privileged: bool | None
    def __init__(self, privileged) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _can_use_icmp_lib_with_privilege() -> None | bool: ...
