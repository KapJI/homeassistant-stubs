from .core import HomeAssistant as HomeAssistant, callback as callback
from .exceptions import HomeAssistantError as HomeAssistantError
from .helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from .loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any

PIP_TIMEOUT: int
MAX_INSTALL_FAILURES: int
DATA_PIP_LOCK: str
DATA_PKG_CACHE: str
DATA_INTEGRATIONS_WITH_REQS: str
DATA_INSTALL_FAILURE_HISTORY: str
CONSTRAINT_FILE: str
DISCOVERY_INTEGRATIONS: dict[str, Iterable[str]]
_LOGGER: Incomplete

class RequirementsNotFound(HomeAssistantError):
    domain: Incomplete
    requirements: Incomplete
    def __init__(self, domain: str, requirements: list[str]) -> None: ...

async def async_get_integration_with_requirements(hass: HomeAssistant, domain: str, done: Union[set[str], None] = ...) -> Integration: ...
async def _async_process_integration(hass: HomeAssistant, integration: Integration, done: set[str]) -> None: ...
def async_clear_install_history(hass: HomeAssistant) -> None: ...
async def async_process_requirements(hass: HomeAssistant, name: str, requirements: list[str]) -> None: ...
async def _async_process_requirements(hass: HomeAssistant, name: str, req: str, install_failure_history: set[str], kwargs: Any) -> None: ...
def pip_kwargs(config_dir: Union[str, None]) -> dict[str, Any]: ...
