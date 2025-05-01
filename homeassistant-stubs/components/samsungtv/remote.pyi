from .const import LOGGER as LOGGER
from .coordinator import SamsungTVConfigEntry as SamsungTVConfigEntry
from .entity import SamsungTVEntity as SamsungTVEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: SamsungTVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SamsungTVRemote(SamsungTVEntity, RemoteEntity):
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
