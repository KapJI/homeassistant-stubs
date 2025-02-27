from .coordinator import StarlinkConfigEntry as StarlinkConfigEntry, StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: StarlinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[StarlinkUpdateCoordinator], Awaitable[None]]

class StarlinkButtonEntity(StarlinkEntity, ButtonEntity):
    entity_description: StarlinkButtonEntityDescription
    async def async_press(self) -> None: ...

BUTTONS: Incomplete
