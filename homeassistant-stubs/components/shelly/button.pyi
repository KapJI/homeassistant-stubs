from .const import LOGGER as LOGGER, SHELLY_GAS_MODELS as SHELLY_GAS_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .utils import get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Any, Final, Generic, TypeVar

_ShellyCoordinatorT = TypeVar('_ShellyCoordinatorT', bound=ShellyBlockCoordinator | ShellyRpcCoordinator)

@dataclass
class ShellyButtonDescriptionMixin(Generic[_ShellyCoordinatorT]):
    press_action: Callable[[_ShellyCoordinatorT], Coroutine[Any, Any, None]]
    def __init__(self, press_action) -> None: ...

@dataclass
class ShellyButtonDescription(ButtonEntityDescription, ShellyButtonDescriptionMixin[_ShellyCoordinatorT]):
    supported: Callable[[_ShellyCoordinatorT], bool] = ...
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, supported) -> None: ...

BUTTONS: Final[list[ShellyButtonDescription[Any]]]

def async_migrate_unique_ids(entity_entry: er.RegistryEntry, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator) -> dict[str, Any] | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyButton(CoordinatorEntity[ShellyRpcCoordinator | ShellyBlockCoordinator], ButtonEntity):
    entity_description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]) -> None: ...
    async def async_press(self) -> None: ...
