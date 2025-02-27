from . import IronOSConfigEntry as IronOSConfigEntry
from .coordinator import IronOSCoordinators as IronOSCoordinators
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynecil import CharSetting

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IronOSButtonEntityDescription(ButtonEntityDescription):
    characteristic: CharSetting

class IronOSButton(StrEnum):
    SETTINGS_RESET = 'settings_reset'
    SETTINGS_SAVE = 'settings_save'

BUTTON_DESCRIPTIONS: tuple[IronOSButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IronOSButtonEntity(IronOSBaseEntity, ButtonEntity):
    entity_description: IronOSButtonEntityDescription
    settings: Incomplete
    def __init__(self, coordinators: IronOSCoordinators, entity_description: IronOSButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
