from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from .utils import alexa_api_call as alexa_api_call
from _typeshed import Incomplete
from aioamazondevices.api import AmazonDevice as AmazonDevice, AmazonEchoApi as AmazonEchoApi
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonNotifyEntityDescription(NotifyEntityDescription):
    is_supported: Callable[[AmazonDevice], bool] = ...
    method: Callable[[AmazonEchoApi, AmazonDevice, str], Awaitable[None]]
    subkey: str

NOTIFY: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonNotifyEntity(AmazonEntity, NotifyEntity):
    entity_description: AmazonNotifyEntityDescription
    @alexa_api_call
    async def async_send_message(self, message: str, title: str | None = None, **kwargs: Any) -> None: ...
