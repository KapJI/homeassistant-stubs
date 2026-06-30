from .const import DOMAIN as DOMAIN, VENTILATION_CAPABLE_NODE_TYPES as VENTILATION_CAPABLE_NODE_TYPES
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from _typeshed import Incomplete
from duco_connectivity import ActionItem as ActionItem, Node as Node, NodeListActionItemList as NodeListActionItemList
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

def _get_ventilation_options(action: ActionItem) -> tuple[str, ...] | None: ...
def _discover_ventilation_options(node_actions: NodeListActionItemList) -> dict[int, tuple[str, ...]]: ...
async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoVentilationStateSelect(DucoEntity, SelectEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node, options: tuple[str, ...]) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
