from .const import DOMAIN as DOMAIN
from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevice as AmazonDevice, alexa_api_call as alexa_api_call
from .entity import AmazonEntity as AmazonEntity, AmazonServiceEntity as AmazonServiceEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonSelectEntityDescription(SelectEntityDescription):
    method: str
    is_available_fn: Callable[[AmazonDevice], bool] = ...

SELECTS: Final[Incomplete]
SERVICE_SELECTS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonSelectEntity(AmazonEntity, SelectEntity):
    entity_description: AmazonSelectEntityDescription
    @property
    @override
    def options(self) -> list[str]: ...
    @property
    def _device(self) -> AmazonDevice: ...
    _attr_current_option: Incomplete
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...

class AmazonSelectServiceEntity(AmazonServiceEntity, SelectEntity):
    entity_description: AmazonSelectEntityDescription
    @property
    @override
    def options(self) -> list[str]: ...
    _attr_current_option: Incomplete
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
