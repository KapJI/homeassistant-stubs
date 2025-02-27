from .const import DOMAIN as DOMAIN
from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from .entity import CookidooBaseEntity as CookidooBaseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from cookidoo_api import Cookidoo as Cookidoo
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CookidooButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Cookidoo], Awaitable[None]]

TODO_CLEAR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: CookidooConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CookidooButton(CookidooBaseEntity, ButtonEntity):
    entity_description: CookidooButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator, description: CookidooButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
