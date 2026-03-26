from .coordinator import TransmissionConfigEntry as TransmissionConfigEntry, TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from .entity import TransmissionEntity as TransmissionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TransmissionBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[TransmissionDataUpdateCoordinator], bool | None]

BINARY_SENSOR_TYPES: tuple[TransmissionBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TransmissionBinarySensor(TransmissionEntity, BinarySensorEntity):
    entity_description: TransmissionBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
