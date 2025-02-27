from .const import SUBSCRIPTION_MAP as SUBSCRIPTION_MAP
from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooData as CookidooData, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from .entity import CookidooBaseEntity as CookidooBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class CookidooSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[CookidooData], StateType | datetime]

class CookidooSensor(StrEnum):
    SUBSCRIPTION = 'subscription'
    EXPIRES = 'expires'

SENSOR_DESCRIPTIONS: tuple[CookidooSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: CookidooConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CookidooSensorEntity(CookidooBaseEntity, SensorEntity):
    entity_description: CookidooSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator, entity_description: CookidooSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
