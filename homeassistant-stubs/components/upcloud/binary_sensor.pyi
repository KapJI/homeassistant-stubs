from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry
from .entity import UpCloudServerEntity as UpCloudServerEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: UpCloudConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UpCloudBinarySensor(UpCloudServerEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
