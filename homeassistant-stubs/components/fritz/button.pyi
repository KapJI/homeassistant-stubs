from .const import BUTTON_TYPE_WOL as BUTTON_TYPE_WOL, CONNECTION_TYPE_LAN as CONNECTION_TYPE_LAN, MeshRoles as MeshRoles
from .coordinator import AvmWrapper as AvmWrapper, FRITZ_DATA_KEY as FRITZ_DATA_KEY, FritzConfigEntry as FritzConfigEntry, FritzData as FritzData
from .entity import FritzDeviceBase as FritzDeviceBase
from .helpers import _is_tracked as _is_tracked
from .models import FritzDevice as FritzDevice
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FritzButtonDescription(ButtonEntityDescription):
    press_action: Callable[[AvmWrapper], Any]

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: FritzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FritzButton(ButtonEntity):
    entity_description: FritzButtonDescription
    _attr_has_entity_name: bool
    avm_wrapper: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, description: FritzButtonDescription) -> None: ...
    async def async_press(self) -> None: ...

@callback
def _async_wol_buttons_list(avm_wrapper: AvmWrapper, data_fritz: FritzData) -> list[FritzBoxWOLButton]: ...

class FritzBoxWOLButton(FritzDeviceBase, ButtonEntity):
    _attr_icon: str
    _attr_entity_registry_enabled_default: bool
    _name: Incomplete
    _attr_unique_id: Incomplete
    _is_available: bool
    def __init__(self, avm_wrapper: AvmWrapper, device: FritzDevice) -> None: ...
    async def async_press(self) -> None: ...
