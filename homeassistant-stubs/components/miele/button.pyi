from .const import DOMAIN as DOMAIN, MieleActions as MieleActions, MieleAppliance as MieleAppliance, PROCESS_ACTION as PROCESS_ACTION
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleButtonDescription(ButtonEntityDescription):
    press_data: MieleActions

@dataclass
class MieleButtonDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleButtonDescription

BUTTON_TYPES: Final[tuple[MieleButtonDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleButton(MieleEntity, ButtonEntity):
    entity_description: MieleButtonDescription
    @property
    def available(self) -> bool: ...
    async def async_press(self) -> None: ...
