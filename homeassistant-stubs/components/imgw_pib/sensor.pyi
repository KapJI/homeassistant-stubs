from .const import DOMAIN as DOMAIN
from .coordinator import ImgwPibConfigEntry as ImgwPibConfigEntry, ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from .entity import ImgwPibEntity as ImgwPibEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from imgw_pib.model import HydrologicalData as HydrologicalData
from typing import Any

PARALLEL_UPDATES: int

def gen_alert_attributes(data: HydrologicalData) -> dict[str, Any] | None: ...

@dataclass(frozen=True, kw_only=True)
class ImgwPibSensorEntityDescription(SensorEntityDescription):
    value: Callable[[HydrologicalData], StateType]
    attrs: Callable[[HydrologicalData], dict[str, Any] | None] | None = ...

SENSOR_TYPES: tuple[ImgwPibSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ImgwPibSensorEntity(ImgwPibEntity, SensorEntity):
    entity_description: ImgwPibSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ImgwPibDataUpdateCoordinator, description: ImgwPibSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
