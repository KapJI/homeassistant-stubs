from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute

PARALLEL_UPDATES: int
BINARY_SENSOR_DESCRIPTIONS: dict[AttributeType, BinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeBinarySensor(HomeeEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
