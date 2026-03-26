from .coordinator import ArcamFmjConfigEntry as ArcamFmjConfigEntry
from .entity import ArcamFmjEntity as ArcamFmjEntity
from arcam.fmj.state import State as State
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfFrequency as UnitOfFrequency
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class ArcamFmjSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[State], int | float | str | None]

SENSORS: tuple[ArcamFmjSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ArcamFmjConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ArcamFmjSensorEntity(ArcamFmjEntity, SensorEntity):
    entity_description: ArcamFmjSensorEntityDescription
    @property
    def native_value(self) -> int | float | str | None: ...
