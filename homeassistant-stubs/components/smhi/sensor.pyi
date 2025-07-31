from .coordinator import SMHIConfigEntry as SMHIConfigEntry, SMHIDataUpdateCoordinator as SMHIDataUpdateCoordinator
from .entity import SmhiWeatherBaseEntity as SmhiWeatherBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

def get_percentage_values(entity: SMHISensor, key: str) -> int | None: ...

@dataclass(frozen=True, kw_only=True)
class SMHISensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SMHISensor], StateType | datetime]

SENSOR_DESCRIPTIONS: tuple[SMHISensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SMHIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SMHISensor(SmhiWeatherBaseEntity, SensorEntity):
    entity_description: SMHISensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, latitude: str, longitude: str, coordinator: SMHIDataUpdateCoordinator, entity_description: SMHISensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def update_entity_data(self) -> None: ...
