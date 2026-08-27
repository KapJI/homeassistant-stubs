from .coordinator import GatusConfigEntry as GatusConfigEntry, GatusDataUpdateCoordinator as GatusDataUpdateCoordinator
from .entity import GatusEndpointEntity as GatusEndpointEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from gatus_api import EndpointStatus as EndpointStatus
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class GatusSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GatusDataUpdateCoordinator, EndpointStatus], datetime | float | int | str | None]

SENSOR_TYPES: tuple[GatusSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GatusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GatusEndpointSensor(GatusEndpointEntity, SensorEntity):
    entity_description: GatusSensorEntityDescription
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GatusDataUpdateCoordinator, entry: GatusConfigEntry, endpoint_key: str, description: GatusSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> datetime | float | int | str | None: ...
