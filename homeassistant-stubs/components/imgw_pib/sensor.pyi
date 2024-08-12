from . import ImgwPibConfigEntry as ImgwPibConfigEntry
from .coordinator import ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from .entity import ImgwPibEntity as ImgwPibEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from imgw_pib.model import HydrologicalData as HydrologicalData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ImgwPibSensorEntityDescription(SensorEntityDescription):
    value: Callable[[HydrologicalData], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value) -> None: ...

SENSOR_TYPES: tuple[ImgwPibSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ImgwPibSensorEntity(ImgwPibEntity, SensorEntity):
    entity_description: ImgwPibSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ImgwPibDataUpdateCoordinator, description: ImgwPibSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
