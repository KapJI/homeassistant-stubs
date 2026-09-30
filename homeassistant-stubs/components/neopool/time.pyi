import asyncio
from .const import CONF_USE_AUX1 as CONF_USE_AUX1, CONF_USE_AUX2 as CONF_USE_AUX2, CONF_USE_AUX3 as CONF_USE_AUX3, CONF_USE_AUX4 as CONF_USE_AUX4, CONF_USE_LIGHT as CONF_USE_LIGHT, DOMAIN as DOMAIN
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry, NeoPoolCoordinator as NeoPoolCoordinator
from .entity import NeoPoolEntity as NeoPoolEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, time as dt_time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any, Literal, override

PARALLEL_UPDATES: int
WRITE_DELAY: Incomplete

@dataclass(frozen=True, kw_only=True)
class NeoPoolTimeEntityDescription(TimeEntityDescription):
    timer_block: str
    timer_field: Literal['start', 'stop']
    supported_fn: Callable[[dict[str, Any], Mapping[str, Any]], bool] | None = ...
    translation_placeholders: dict[str, str] | None = ...

def _option_supported(opt_flag: str) -> Callable[[dict[str, Any], Mapping[str, Any]], bool]: ...
def _light_supported(data: dict[str, Any], opts: Mapping[str, Any]) -> bool: ...

_TIMER_BLOCKS: tuple[tuple[str, str | None, bool], ...]

def _build_descriptions() -> dict[str, NeoPoolTimeEntityDescription]: ...

TIME_DESCRIPTIONS: dict[str, NeoPoolTimeEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NeoPoolTime(NeoPoolEntity, TimeEntity):
    entity_description: NeoPoolTimeEntityDescription
    _key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _write_unsub: CALLBACK_TYPE | None
    _pending_value: int | None
    _pending_token: int
    _write_future: asyncio.Future[Exception | None] | None
    _flush_lock: Incomplete
    _flush_tasks: set[asyncio.Task[None]]
    _removing: bool
    def __init__(self, coordinator: NeoPoolCoordinator, key: str, description: NeoPoolTimeEntityDescription) -> None: ...
    def _decode_raw(self) -> dt_time | None: ...
    @property
    @override
    def native_value(self) -> dt_time | None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _cancel_pending_write(self) -> None: ...
    @override
    async def async_set_value(self, value: dt_time) -> None: ...
    @callback
    def _schedule_flush(self, _now: datetime) -> None: ...
    async def _async_flush(self, future: asyncio.Future[Exception | None] | None, pending: int | None, token: int) -> None: ...
    @callback
    def _abort_if_removing(self, future: asyncio.Future[Exception | None] | None) -> bool: ...
    @callback
    def _report_write_failure(self, future: asyncio.Future[Exception | None] | None, batch_token: int, exc: Exception) -> None: ...
    @callback
    def _clear_pending_if_current(self, batch_token: int) -> None: ...
