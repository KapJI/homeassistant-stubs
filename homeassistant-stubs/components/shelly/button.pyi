from .const import SHELLY_GAS_MODELS as SHELLY_GAS_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .utils import get_block_device_name as get_block_device_name, get_device_entry_gen as get_device_entry_gen, get_rpc_device_name as get_rpc_device_name
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Final

class ShellyButtonDescriptionMixin:
    press_action: Callable
    def __init__(self, press_action) -> None: ...

class ShellyButtonDescription(ButtonEntityDescription, ShellyButtonDescriptionMixin):
    supported: Callable
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, supported) -> None: ...

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyButton(CoordinatorEntity, ButtonEntity):
    entity_description: ShellyButtonDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: Union[ShellyRpcCoordinator, ShellyBlockCoordinator], description: ShellyButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
