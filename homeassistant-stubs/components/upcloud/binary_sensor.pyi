from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry
from .entity import UpCloudServerEntity as UpCloudServerEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: UpCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UpCloudBinarySensor(UpCloudServerEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
