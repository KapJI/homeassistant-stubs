from . import SwitcherConfigEntry as SwitcherConfigEntry
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .utils import get_breeze_remote_manager as get_breeze_remote_manager
from _typeshed import Incomplete
from aioswitcher.api import SwitcherApi as SwitcherApi, SwitcherBaseResponse as SwitcherBaseResponse
from aioswitcher.api.remotes import SwitcherBreezeRemote
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SwitcherThermostatButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[SwitcherApi, SwitcherBreezeRemote], Coroutine[Any, Any, SwitcherBaseResponse]]
    supported: Callable[[SwitcherBreezeRemote], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_fn, supported) -> None: ...

THERMOSTAT_BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: SwitcherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherThermostatButtonEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], ButtonEntity):
    entity_description: SwitcherThermostatButtonEntityDescription
    _attr_has_entity_name: bool
    _remote: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, description: SwitcherThermostatButtonEntityDescription, remote: SwitcherBreezeRemote) -> None: ...
    async def async_press(self) -> None: ...
