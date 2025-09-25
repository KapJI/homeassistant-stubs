from . import HomeeConfigEntry as HomeeConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from enum import IntEnum
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeNode as HomeeNode
from typing import Any

_LOGGER: Incomplete

async def setup_homee_platform(add_platform_entities: Callable[[HomeeConfigEntry, AddConfigEntryEntitiesCallback, list[HomeeNode]], Coroutine[Any, Any, None]], async_add_entities: AddConfigEntryEntitiesCallback, config_entry: HomeeConfigEntry) -> None: ...
def get_name_for_enum(att_class: type[IntEnum], att_id: int) -> str | None: ...
