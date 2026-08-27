from .const import ATTR_DATA as ATTR_DATA, DEVICE_MODEL_ACCOUNT as DEVICE_MODEL_ACCOUNT, DOMAIN as DOMAIN, EVENT_TRANSACTION_CREATED as EVENT_TRANSACTION_CREATED, NON_TRANSFER_ACCOUNT_TYPES as NON_TRANSFER_ACCOUNT_TYPES
from .coordinator import MonzoConfigEntry as MonzoConfigEntry
from .helpers import get_account_name as get_account_name
from .webhook import webhook_signal as webhook_signal
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: MonzoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MonzoTransactionEvent(EventEntity):
    _attr_attribution: str
    _attr_event_types: Incomplete
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _account_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, account: dict[str, Any]) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event_type: str, transaction: dict[str, Any]) -> None: ...
