from . import IndevoltConfigEntry as IndevoltConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltSwitchEntityDescription(SwitchEntityDescription):
    read_key: str
    write_key: str
    read_on_value: int = ...
    read_off_value: int = ...
    generation: tuple[int, ...] = ...

SWITCHES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltSwitchEntity(IndevoltEntity, SwitchEntity):
    entity_description: IndevoltSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_toggle(self, value: int) -> None: ...
