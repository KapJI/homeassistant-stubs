from .coordinator import VizioConfigEntry as VizioConfigEntry, VizioDeviceData as VizioDeviceData
from .entity import VizioDescriptionEntity as VizioDescriptionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VizioSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[VizioDeviceData], int | None]

SENSORS: tuple[VizioSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: VizioConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VizioSensor(VizioDescriptionEntity, SensorEntity):
    entity_description: VizioSensorEntityDescription
    @property
    @override
    def native_value(self) -> int | None: ...
