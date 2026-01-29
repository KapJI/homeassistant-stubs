from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .entity import MastodonEntity as MastodonEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from mastodon.Mastodon import Account as Account

PARALLEL_UPDATES: int

class MastodonBinarySensor(StrEnum):
    BOT = 'bot'
    SUSPENDED = 'suspended'
    DISCOVERABLE = 'discoverable'
    LOCKED = 'locked'
    INDEXABLE = 'indexable'
    LIMITED = 'limited'
    MEMORIAL = 'memorial'
    MOVED = 'moved'

@dataclass(frozen=True, kw_only=True)
class MastodonBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Account], bool | None]

ENTITY_DESCRIPTIONS: tuple[MastodonBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MastodonBinarySensorEntity(MastodonEntity, BinarySensorEntity):
    entity_description: MastodonBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
