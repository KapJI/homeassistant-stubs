from .coordinator import StreamlabsConfigEntry as StreamlabsConfigEntry, StreamlabsCoordinator as StreamlabsCoordinator, StreamlabsData as StreamlabsData
from .entity import StreamlabsWaterEntity as StreamlabsWaterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class StreamlabsWaterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StreamlabsData], StateType]

SENSORS: tuple[StreamlabsWaterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class StreamLabsSensor(StreamlabsWaterEntity, SensorEntity):
    entity_description: StreamlabsWaterSensorEntityDescription
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str, entity_description: StreamlabsWaterSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
