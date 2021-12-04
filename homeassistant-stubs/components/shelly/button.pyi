from . import BlockDeviceWrapper as BlockDeviceWrapper, RpcDeviceWrapper as RpcDeviceWrapper
from .const import BLOCK as BLOCK, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, RPC as RPC
from .utils import get_block_device_name as get_block_device_name, get_device_entry_gen as get_device_entry_gen, get_rpc_device_name as get_rpc_device_name
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Any, Final

class ShellyButtonDescriptionMixin:
    press_action: Callable

class ShellyButtonDescription(ButtonEntityDescription, ShellyButtonDescriptionMixin): ...

BUTTONS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyButton(ButtonEntity):
    entity_description: ShellyButtonDescription
    wrapper: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, wrapper: Union[RpcDeviceWrapper, BlockDeviceWrapper], description: ShellyButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
