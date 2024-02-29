from . import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import MyUplinkEntity as MyUplinkEntity
from .helpers import find_matching_platform as find_matching_platform
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from myuplink import DevicePoint as DevicePoint

CATEGORY_BASED_DESCRIPTIONS: dict[str, dict[str, BinarySensorEntityDescription]]

def get_description(device_point: DevicePoint) -> BinarySensorEntityDescription | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDevicePointBinarySensor(MyUplinkEntity, BinarySensorEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: BinarySensorEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
