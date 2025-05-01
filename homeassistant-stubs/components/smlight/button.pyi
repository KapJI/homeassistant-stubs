from .const import DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry, SmDataUpdateCoordinator as SmDataUpdateCoordinator
from .entity import SmEntity as SmEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysmlight.web import CmdWrapper as CmdWrapper

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SmButtonDescription(ButtonEntityDescription):
    press_fn: Callable[[CmdWrapper], Awaitable[None]]

BUTTONS: list[SmButtonDescription]
ROUTER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmButton(SmEntity, ButtonEntity):
    coordinator: SmDataUpdateCoordinator
    entity_description: SmButtonDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SmDataUpdateCoordinator, description: SmButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
