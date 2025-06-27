from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from .utils import alexa_api_call as alexa_api_call
from _typeshed import Incomplete
from aioamazondevices.api import AmazonDevice as AmazonDevice
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
    subkey: str
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
