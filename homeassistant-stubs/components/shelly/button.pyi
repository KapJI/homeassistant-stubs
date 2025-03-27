from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SHELLY_GAS_MODELS as SHELLY_GAS_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .utils import get_device_entry_gen as get_device_entry_gen, get_rpc_key_ids as get_rpc_key_ids
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class ShellyButtonDescription[_ShellyCoordinatorT: ShellyBlockCoordinator | ShellyRpcCoordinator](ButtonEntityDescription):
    press_action: str
    supported: Callable[[_ShellyCoordinatorT], bool] = ...

BUTTONS: Final[list[ShellyButtonDescription[Any]]]
BLU_TRV_BUTTONS: Final[list[ShellyButtonDescription]]

@callback
def async_migrate_unique_ids(coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, entity_entry: er.RegistryEntry) -> dict[str, Any] | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ShellyBaseButton(CoordinatorEntity[ShellyRpcCoordinator | ShellyBlockCoordinator], ButtonEntity):
    entity_description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]
    def __init__(self, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]) -> None: ...
    async def async_press(self) -> None: ...
    async def _press_method(self) -> None: ...

class ShellyButton(ShellyBaseButton):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]) -> None: ...
    async def _press_method(self) -> None: ...

class ShellyBluTrvButton(ShellyBaseButton):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _id: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, description: ShellyButtonDescription, id_: int) -> None: ...
    async def _press_method(self) -> None: ...
