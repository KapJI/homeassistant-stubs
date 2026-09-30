from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator, alexa_api_call as alexa_api_call
from .entity import AmazonEntity as AmazonEntity
from .utils import async_remove_entities as async_remove_entities, async_update_unique_id as async_update_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final, override

PARALLEL_UPDATES: int

def _communication_is_on(coordinator: AmazonDevicesCoordinator, serial_num: str, entity_description_key: str) -> bool: ...
def _update_communication_state(coordinator: AmazonDevicesCoordinator, serial_num: str, entity_description_key: str, state: bool) -> None: ...

@dataclass(frozen=True, kw_only=True)
class AmazonSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[AmazonDevicesCoordinator, str, str], bool]
    is_available_fn: Callable[[AmazonDevicesCoordinator, str, str], bool]
    method: str
    update_state_fn: Callable[[AmazonDevicesCoordinator, str, str, bool], None]

DND_SWITCH: Final[Incomplete]
COMMUNICATION_SWITCHES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonSwitchEntity(AmazonEntity, SwitchEntity):
    entity_description: AmazonSwitchEntityDescription
    async def _switch_set_state(self, state: bool) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def available(self) -> bool: ...
