from .coordinator import SMHIConfigEntry as SMHIConfigEntry, SMHIDataUpdateCoordinator as SMHIDataUpdateCoordinator, SMHIFireDataUpdateCoordinator as SMHIFireDataUpdateCoordinator
from .entity import SmhiFireEntity as SmhiFireEntity, SmhiWeatherEntity as SmhiWeatherEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, PERCENTAGE as PERCENTAGE, UnitOfSpeed as UnitOfSpeed
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int
FWI_INDEX_MAP: Incomplete
GRASSFIRE_MAP: Incomplete
FORESTDRY_MAP: Incomplete

def get_percentage_values(entity: SMHIWeatherSensor, key: str) -> int | None: ...
def get_fire_index_value(entity: SMHIFireSensor, key: str) -> str: ...

@dataclass(frozen=True, kw_only=True)
class SMHIWeatherEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SMHIWeatherSensor], StateType | datetime]

@dataclass(frozen=True, kw_only=True)
class SMHIFireEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SMHIFireSensor], StateType | datetime]

WEATHER_SENSOR_DESCRIPTIONS: tuple[SMHIWeatherEntityDescription, ...]
FIRE_SENSOR_DESCRIPTIONS: tuple[SMHIFireEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SMHIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SMHIWeatherSensor(SmhiWeatherEntity, SensorEntity):
    entity_description: SMHIWeatherEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIDataUpdateCoordinator, entity_description: SMHIWeatherEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def update_entity_data(self) -> None: ...

class SMHIFireSensor(SmhiFireEntity, SensorEntity):
    entity_description: SMHIFireEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIFireDataUpdateCoordinator, entity_description: SMHIFireEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def update_entity_data(self) -> None: ...
