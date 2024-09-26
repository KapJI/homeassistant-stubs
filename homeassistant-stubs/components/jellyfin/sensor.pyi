from . import JellyfinConfigEntry as JellyfinConfigEntry
from .coordinator import JellyfinDataT as JellyfinDataT
from .entity import JellyfinEntity as JellyfinEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class JellyfinSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[JellyfinDataT], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

def _count_now_playing(data: JellyfinDataT) -> int: ...

SENSOR_TYPES: dict[str, JellyfinSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: JellyfinConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JellyfinSensor(JellyfinEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: JellyfinSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
