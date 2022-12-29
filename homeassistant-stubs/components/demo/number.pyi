from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoNumber(NumberEntity):
    _attr_should_poll: bool
    _attr_assumed_state: Incomplete
    _attr_device_class: Incomplete
    _attr_icon: Incomplete
    _attr_mode: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, name: str, state: float, icon: str, assumed_state: bool, *, device_class: Union[NumberDeviceClass, None] = ..., mode: NumberMode = ..., native_min_value: Union[float, None] = ..., native_max_value: Union[float, None] = ..., native_step: Union[float, None] = ..., unit_of_measurement: Union[str, None] = ...) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
