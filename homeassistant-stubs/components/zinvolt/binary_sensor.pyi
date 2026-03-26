from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry, ZinvoltData as ZinvoltData, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from .entity import ZinvoltEntity as ZinvoltEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

POINT_ENTITIES: Incomplete

@dataclass(kw_only=True, frozen=True)
class ZinvoltBatteryStateDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[ZinvoltData], bool]

SENSORS: tuple[ZinvoltBatteryStateDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZinvoltBatteryStateBinarySensor(ZinvoltEntity, BinarySensorEntity):
    entity_description: ZinvoltBatteryStateDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator, description: ZinvoltBatteryStateDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class ZinvoltPointBinarySensor(ZinvoltEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    point: Incomplete
    _attr_translation_key: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator, point: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
