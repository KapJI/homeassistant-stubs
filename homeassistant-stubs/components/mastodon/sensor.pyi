from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .entity import MastodonEntity as MastodonEntity
from .utils import construct_mastodon_username as construct_mastodon_username
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from mastodon.Mastodon import Account as Account, Instance as Instance, InstanceV2 as InstanceV2
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MastodonSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Account, InstanceV2 | Instance], StateType | datetime]
    attributes_fn: Callable[[Account], Mapping[str, Any]] | None = ...
    entity_picture_fn: Callable[[Account], str] | None = ...

def account_meta(data: Account) -> Mapping[str, Any]: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MastodonSensorEntity(MastodonEntity, SensorEntity):
    entity_description: MastodonSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    @property
    def entity_picture(self) -> str | None: ...
