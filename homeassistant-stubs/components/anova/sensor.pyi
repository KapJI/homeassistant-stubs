from .coordinator import AnovaCoordinator as AnovaCoordinator
from .entity import AnovaDescriptionEntity as AnovaDescriptionEntity
from .models import AnovaConfigEntry as AnovaConfigEntry
from anova_wifi import APCUpdateSensor as APCUpdateSensor
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class AnovaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[APCUpdateSensor], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SENSOR_DESCRIPTIONS: list[AnovaSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: AnovaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def setup_coordinator(coordinator: AnovaCoordinator, async_add_entities: AddEntitiesCallback) -> None: ...

class AnovaSensor(AnovaDescriptionEntity, SensorEntity):
    entity_description: AnovaSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
