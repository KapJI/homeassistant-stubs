from . import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import MyUplinkEntity as MyUplinkEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from myuplink.models import DevicePoint as DevicePoint

DEVICE_POINT_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkDevicePointSensor(MyUplinkEntity, SensorEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: SensorEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
