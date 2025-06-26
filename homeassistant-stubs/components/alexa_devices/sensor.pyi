from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from .entity import AmazonEntity as AmazonEntity
from _typeshed import Incomplete
from aioamazondevices.api import AmazonDevice as AmazonDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonSensorEntityDescription(SensorEntityDescription):
    native_unit_of_measurement_fn: Callable[[AmazonDevice, str], str] | None = ...

SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonSensorEntity(AmazonEntity, SensorEntity):
    entity_description: AmazonSensorEntityDescription
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType: ...
