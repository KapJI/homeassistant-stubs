from .const import ASSETS_URL as ASSETS_URL
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry
from .entity import HabiticaBase as HabiticaBase
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from habiticalib import UserData as UserData
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HabiticaBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[UserData], bool | None]
    entity_picture: Callable[[UserData], str | None]

class HabiticaBinarySensor(StrEnum):
    PENDING_QUEST = 'pending_quest'

def get_scroll_image_for_pending_quest_invitation(user: UserData) -> str | None: ...

BINARY_SENSOR_DESCRIPTIONS: tuple[HabiticaBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaBinarySensorEntity(HabiticaBase, BinarySensorEntity):
    entity_description: HabiticaBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    @property
    def entity_picture(self) -> str | None: ...
