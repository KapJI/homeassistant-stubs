from .const import DOMAIN as DOMAIN
from .coordinator import TailwindConfigEntry as TailwindConfigEntry
from .entity import TailwindEntity as TailwindEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from gotailwind import Tailwind as Tailwind
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TailwindButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Tailwind], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TailwindConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TailwindButtonEntity(TailwindEntity, ButtonEntity):
    entity_description: TailwindButtonEntityDescription
    async def async_press(self) -> None: ...
