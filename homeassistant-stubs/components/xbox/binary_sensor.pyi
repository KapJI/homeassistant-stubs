from .coordinator import XboxConfigEntry as XboxConfigEntry
from .entity import XboxBaseEntity as XboxBaseEntity, XboxBaseEntityDescription as XboxBaseEntityDescription, check_deprecated_entity as check_deprecated_entity, profile_pic as profile_pic
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.titlehub.models import Title as Title
from typing import Any

PARALLEL_UPDATES: int

class XboxBinarySensor(StrEnum):
    ONLINE = 'online'
    IN_PARTY = 'in_party'
    IN_GAME = 'in_game'
    IN_MULTIPLAYER = 'in_multiplayer'
    HAS_GAME_PASS = 'has_game_pass'

@dataclass(kw_only=True, frozen=True)
class XboxBinarySensorEntityDescription(XboxBaseEntityDescription, BinarySensorEntityDescription):
    is_on_fn: Callable[[Person], bool | None]

def profile_attributes(person: Person, _: Title | None) -> dict[str, Any]: ...
def in_game(person: Person) -> bool: ...

SENSOR_DESCRIPTIONS: tuple[XboxBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class XboxBinarySensorEntity(XboxBaseEntity, BinarySensorEntity):
    entity_description: XboxBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
