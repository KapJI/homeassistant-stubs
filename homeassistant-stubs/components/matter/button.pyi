from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import MatterConfigEntry as MatterConfigEntry
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: MatterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterButtonEntityDescription(ButtonEntityDescription, MatterEntityDescription):
    command: Callable[[], Any] | None = ...

class MatterCommandButton(MatterEntity, ButtonEntity):
    entity_description: MatterButtonEntityDescription
    async def async_press(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
