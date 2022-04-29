from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

CHARGING_SUFFIX: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserBatteryChargingBinarySensor(DiffuserEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
