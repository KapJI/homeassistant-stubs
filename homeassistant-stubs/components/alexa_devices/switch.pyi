from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from .utils import alexa_api_call as alexa_api_call, async_remove_dnd_from_virtual_group as async_remove_dnd_from_virtual_group, async_update_unique_id as async_update_unique_id
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonDevice as AmazonDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[AmazonDevice], bool]
    is_available_fn: Callable[[AmazonDevice, str], bool] = ...
    method: str

SWITCHES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonSwitchEntity(AmazonEntity, SwitchEntity):
    entity_description: AmazonSwitchEntityDescription
    @alexa_api_call
    async def _switch_set_state(self, state: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
