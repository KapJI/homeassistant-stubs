from collections.abc import Iterable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any

DATA_PIP_LOCK: str
DATA_PKG_CACHE: str
DATA_INTEGRATIONS_WITH_REQS: str
CONSTRAINT_FILE: str
DISCOVERY_INTEGRATIONS: dict[str, Iterable[str]]

class RequirementsNotFound(HomeAssistantError):
    domain: Any
    requirements: Any
    def __init__(self, domain: str, requirements: list[str]) -> None: ...

async def async_get_integration_with_requirements(hass: HomeAssistant, domain: str, done: Union[set[str], None] = ...) -> Integration: ...
async def _async_process_integration(hass: HomeAssistant, integration: Integration, done: set[str]) -> None: ...
async def async_process_requirements(hass: HomeAssistant, name: str, requirements: list[str]) -> None: ...
def pip_kwargs(config_dir: Union[str, None]) -> dict[str, Any]: ...
