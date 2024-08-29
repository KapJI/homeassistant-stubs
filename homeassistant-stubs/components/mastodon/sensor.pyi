from . import MastodonConfigEntry as MastodonConfigEntry
from .const import ACCOUNT_FOLLOWERS_COUNT as ACCOUNT_FOLLOWERS_COUNT, ACCOUNT_FOLLOWING_COUNT as ACCOUNT_FOLLOWING_COUNT, ACCOUNT_STATUSES_COUNT as ACCOUNT_STATUSES_COUNT
from .entity import MastodonEntity as MastodonEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class MastodonSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MastodonSensorEntity(MastodonEntity, SensorEntity):
    entity_description: MastodonSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
