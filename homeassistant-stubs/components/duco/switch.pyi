from .const import DOMAIN as DOMAIN
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from .helpers import remove_stale_node_ids as remove_stale_node_ids
from _typeshed import Incomplete
from duco_connectivity import Node as Node, NodeListActionItemList as NodeListActionItemList
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

def _discover_identify_nodes(node_actions: NodeListActionItemList) -> set[int]: ...
async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoIdentifySwitch(DucoEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_identify(self, identify: bool) -> None: ...
