from .const import DOMAIN as DOMAIN
from .entity import LyngdorfEntity as LyngdorfEntity
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver, Remote as Remote
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LyngdorfRemote(LyngdorfEntity, RemoteEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, receiver: LyngdorfReceiver, config_entry: LyngdorfConfigEntry, device_info: DeviceInfo) -> None: ...
    @property
    def _remote(self) -> Remote: ...
    @override
    @property
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
