from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from eheimdigital.device import EheimDigitalDevice as EheimDigitalDevice
from eheimdigital.reeflex import EheimDigitalReeflexUV
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EheimDigitalBinarySensorDescription[_DeviceT: EheimDigitalDevice](BinarySensorEntityDescription):
    value_fn: Callable[[_DeviceT], bool | None]

REEFLEX_DESCRIPTIONS: tuple[EheimDigitalBinarySensorDescription[EheimDigitalReeflexUV], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalBinarySensor[_DeviceT: EheimDigitalDevice](EheimDigitalEntity[_DeviceT], BinarySensorEntity):
    entity_description: EheimDigitalBinarySensorDescription[_DeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT, description: EheimDigitalBinarySensorDescription[_DeviceT]) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
