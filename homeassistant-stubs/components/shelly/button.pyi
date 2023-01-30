from .const import SHELLY_GAS_MODELS as SHELLY_GAS_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .utils import get_block_device_name as get_block_device_name, get_device_entry_gen as get_device_entry_gen, get_rpc_device_name as get_rpc_device_name
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Any, Final, TypeVar

_ShellyCoordinatorT = TypeVar('_ShellyCoordinatorT', bound=ShellyBlockCoordinator | ShellyRpcCoordinator)

class ShellyButtonDescriptionMixin:
    press_action: Callable[[_ShellyCoordinatorT], Coroutine[Any, Any, None]]
    def __init__(self, press_action) -> None: ...

class ShellyButtonDescription(ButtonEntityDescription, ShellyButtonDescriptionMixin[_ShellyCoordinatorT]):
    supported: Callable[[_ShellyCoordinatorT], bool]
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, supported) -> None: ...

BUTTONS: Final[list[ShellyButtonDescription[Any]]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyButton(CoordinatorEntity[ShellyRpcCoordinator | ShellyBlockCoordinator], ButtonEntity):
    entity_description: ShellyButtonDescription[Union[ShellyRpcCoordinator, ShellyBlockCoordinator]]
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: Union[ShellyRpcCoordinator, ShellyBlockCoordinator], description: ShellyButtonDescription[Union[ShellyRpcCoordinator, ShellyBlockCoordinator]]) -> None: ...
    async def async_press(self) -> None: ...
