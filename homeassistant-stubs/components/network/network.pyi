from .const import ATTR_CONFIGURED_ADAPTERS as ATTR_CONFIGURED_ADAPTERS, DEFAULT_CONFIGURED_ADAPTERS as DEFAULT_CONFIGURED_ADAPTERS, DOMAIN as DOMAIN, STORAGE_KEY as STORAGE_KEY, STORAGE_VERSION as STORAGE_VERSION
from .models import Adapter as Adapter
from .util import async_load_adapters as async_load_adapters, enable_adapters as enable_adapters, enable_auto_detected_adapters as enable_auto_detected_adapters
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any

_LOGGER: Incomplete
DATA_NETWORK: HassKey[Network]

@callback
def async_get_loaded_network(hass: HomeAssistant) -> Network: ...
async def async_get_network(hass: HomeAssistant) -> Network: ...

class Network:
    _store: Incomplete
    _data: dict[str, list[str]]
    adapters: list[Adapter]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def configured_adapters(self) -> list[str]: ...
    async def async_setup(self) -> None: ...
    @callback
    def async_configure(self) -> None: ...
    async def async_reconfig(self, config: dict[str, Any]) -> None: ...
    async def async_load(self) -> None: ...
    async def _async_save(self) -> None: ...
