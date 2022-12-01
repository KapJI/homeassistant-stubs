from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.text import TextEntity as TextEntity, TextMode as TextMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoText(TextEntity):
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_native_value: Incomplete
    _attr_icon: Incomplete
    _attr_mode: Incomplete
    _attr_native_max: Incomplete
    _attr_native_min: Incomplete
    _attr_pattern: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, name: str, icon: Union[str, None], native_value: Union[str, None], mode: TextMode = ..., native_max: Union[int, None] = ..., native_min: Union[int, None] = ..., pattern: Union[str, None] = ...) -> None: ...
    async def async_set_value(self, value: str) -> None: ...
