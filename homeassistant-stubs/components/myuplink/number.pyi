from . import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import MyUplinkEntity as MyUplinkEntity
from .helpers import find_matching_platform as find_matching_platform
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from myuplink import DevicePoint as DevicePoint

DEVICE_POINT_UNIT_DESCRIPTIONS: dict[str, NumberEntityDescription]
CATEGORY_BASED_DESCRIPTIONS: dict[str, dict[str, NumberEntityDescription]]

def get_description(device_point: DevicePoint) -> NumberEntityDescription | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyUplinkNumber(MyUplinkEntity, NumberEntity):
    point_id: Incomplete
    _attr_name: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_step_value: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, device_point: DevicePoint, entity_description: NumberEntityDescription | None, unique_id_suffix: str) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
