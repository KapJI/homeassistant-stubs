from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .entity import MastodonEntity as MastodonEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from mastodon.Mastodon import Account as Account

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MastodonSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Account], StateType]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MastodonSensorEntity(MastodonEntity, SensorEntity):
    entity_description: MastodonSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
