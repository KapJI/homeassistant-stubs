from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoBinarySensor(BinarySensorEntity):
    _attr_should_poll: bool
    _unique_id: Incomplete
    _attr_name: Incomplete
    _state: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, unique_id: str, name: str, state: bool, device_class: BinarySensorDeviceClass) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
