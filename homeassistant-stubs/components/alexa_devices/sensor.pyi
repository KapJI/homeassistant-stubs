from .const import CATEGORY_NOTIFICATIONS as CATEGORY_NOTIFICATIONS, CATEGORY_SENSORS as CATEGORY_SENSORS
from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonDevice as AmazonDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonSensorEntityDescription(SensorEntityDescription):
    native_unit_of_measurement_fn: Callable[[AmazonDevice, str], str] | None = ...
    is_available_fn: Callable[[AmazonDevice, str], bool] = ...
    category: str = ...

@dataclass(frozen=True, kw_only=True)
class AmazonNotificationEntityDescription(SensorEntityDescription):
    native_unit_of_measurement_fn: Callable[[AmazonDevice, str], str] | None = ...
    is_available_fn: Callable[[AmazonDevice, str], bool] = ...
    category: str = ...

SENSORS: Final[Incomplete]
NOTIFICATIONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonSensorEntity(AmazonEntity, SensorEntity):
    entity_description: AmazonSensorEntityDescription | AmazonNotificationEntityDescription
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def available(self) -> bool: ...
