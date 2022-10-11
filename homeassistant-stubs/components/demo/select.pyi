from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoSelect(SelectEntity):
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_current_option: Incomplete
    _attr_icon: Incomplete
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, name: str, icon: str, device_class: Union[str, None], current_option: Union[str, None], options: list[str]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...