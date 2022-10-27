from .const import DOMAIN as DOMAIN
from .coordinator import JellyfinDataT as JellyfinDataT
from .entity import JellyfinEntity as JellyfinEntity
from .models import JellyfinData as JellyfinData
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

class JellyfinSensorEntityDescriptionMixin:
    value_fn: Callable[[JellyfinDataT], StateType]
    def __init__(self, value_fn) -> None: ...

class JellyfinSensorEntityDescription(SensorEntityDescription, JellyfinSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

def _count_now_playing(data: JellyfinDataT) -> int: ...

SENSOR_TYPES: dict[str, JellyfinSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JellyfinSensor(JellyfinEntity, SensorEntity):
    entity_description: JellyfinSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
