from . import VeluxConfigEntry as VeluxConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import VeluxEntity as VeluxEntity, wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import Node, PyVLX as PyVLX

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxIdentifyButton(VeluxEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, node: Node, config_entry_id: str) -> None: ...
    @wrap_pyvlx_call_exceptions
    async def async_press(self) -> None: ...

class VeluxGatewayRebootButton(ButtonEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    pyvlx: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry_id: str, pyvlx: PyVLX) -> None: ...
    async def async_press(self) -> None: ...
