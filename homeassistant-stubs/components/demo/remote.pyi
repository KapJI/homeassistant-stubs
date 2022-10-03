from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import RemoteEntity as RemoteEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities_callback: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class DemoRemote(RemoteEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    _attr_icon: Incomplete
    _last_command_sent: Incomplete
    def __init__(self, name: Union[str, None], state: bool, icon: Union[str, None]) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
