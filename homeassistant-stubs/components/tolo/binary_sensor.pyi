from .coordinator import ToloConfigEntry as ToloConfigEntry, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ToloConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ToloFlowInBinarySensor(ToloSaunaCoordinatorEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...

class ToloFlowOutBinarySensor(ToloSaunaCoordinatorEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
