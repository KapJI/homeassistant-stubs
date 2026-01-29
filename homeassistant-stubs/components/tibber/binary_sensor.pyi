import tibber
from .const import DOMAIN as DOMAIN, TibberConfigEntry as TibberConfigEntry
from .coordinator import TibberDataAPICoordinator as TibberDataAPICoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tibber.data_api import TibberDevice as TibberDevice

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TibberBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[str], bool | None]

DATA_API_BINARY_SENSORS: tuple[TibberBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TibberConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TibberDataAPIBinarySensor(CoordinatorEntity[TibberDataAPICoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: TibberBinarySensorEntityDescription
    _device_id: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TibberDataAPICoordinator, device: TibberDevice, entity_description: TibberBinarySensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> dict[str, tibber.data_api.Sensor]: ...
    @property
    def is_on(self) -> bool | None: ...
