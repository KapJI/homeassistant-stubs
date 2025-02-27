from .coordinator import MinecraftServerConfigEntry as MinecraftServerConfigEntry, MinecraftServerCoordinator as MinecraftServerCoordinator
from .entity import MinecraftServerEntity as MinecraftServerEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

KEY_STATUS: str
BINARY_SENSOR_DESCRIPTIONS: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: MinecraftServerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MinecraftServerBinarySensorEntity(MinecraftServerEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: bool
    def __init__(self, coordinator: MinecraftServerCoordinator, description: BinarySensorEntityDescription, config_entry: MinecraftServerConfigEntry) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
