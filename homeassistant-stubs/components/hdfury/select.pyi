from .const import DOMAIN as DOMAIN
from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry, HDFuryCoordinator as HDFuryCoordinator
from .entity import HDFuryEntity as HDFuryEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HDFurySelectEntityDescription(SelectEntityDescription):
    set_value_fn: Callable[[HDFuryCoordinator, str], Awaitable[None]]

SELECT_PORTS: tuple[HDFurySelectEntityDescription, ...]
SELECT_OPERATION_MODE: HDFurySelectEntityDescription

async def _set_ports(coordinator: HDFuryCoordinator) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HDFurySelect(HDFuryEntity, SelectEntity):
    entity_description: HDFurySelectEntityDescription
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
