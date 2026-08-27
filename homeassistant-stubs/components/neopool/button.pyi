from .const import DOMAIN as DOMAIN
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry, NeoPoolCoordinator as NeoPoolCoordinator
from .entity import NeoPoolEntity as NeoPoolEntity
from .helpers import prepare_device_time as prepare_device_time
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NeoPoolButtonEntityDescription(ButtonEntityDescription):
    supported_fn: Callable[[dict[str, Any]], bool] | None = ...
    press_fn: Callable[[NeoPoolButton], Awaitable[Any]]

BUTTON_DESCRIPTIONS: dict[str, NeoPoolButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NeoPoolButton(NeoPoolEntity, ButtonEntity):
    entity_description: NeoPoolButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NeoPoolCoordinator, key: str, description: NeoPoolButtonEntityDescription) -> None: ...
    @override
    async def async_press(self) -> None: ...
