from .const import DOMAIN as DOMAIN
from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry
from .entity import HDFuryEntity as HDFuryEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from hdfury import HDFuryAPI as HDFuryAPI
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HDFuryButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[HDFuryAPI], Awaitable[None]]

BUTTONS: tuple[HDFuryButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HDFuryButton(HDFuryEntity, ButtonEntity):
    entity_description: HDFuryButtonEntityDescription
    async def async_press(self) -> None: ...
