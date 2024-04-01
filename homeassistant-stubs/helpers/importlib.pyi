from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from types import ModuleType

_LOGGER: Incomplete
DATA_IMPORT_CACHE: str
DATA_IMPORT_FUTURES: str
DATA_IMPORT_FAILURES: str

def _get_module(cache: dict[str, ModuleType], name: str) -> ModuleType: ...
async def async_import_module(hass: HomeAssistant, name: str) -> ModuleType: ...
