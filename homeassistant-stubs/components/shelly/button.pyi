from . import BlockDeviceWrapper as BlockDeviceWrapper, RpcDeviceWrapper as RpcDeviceWrapper
from .const import BLOCK as BLOCK, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, RPC as RPC, SHELLY_GAS_MODELS as SHELLY_GAS_MODELS
from .utils import get_block_device_name as get_block_device_name, get_device_entry_gen as get_device_entry_gen, get_rpc_device_name as get_rpc_device_name
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Any, Final

class ShellyButtonDescriptionMixin:
    press_action: Callable
    def __init__(self, press_action) -> None: ...

class ShellyButtonDescription(ButtonEntityDescription, ShellyButtonDescriptionMixin):
    supported: Callable
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, supported) -> None: ...

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
