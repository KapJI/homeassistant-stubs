from . import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .utils import get_breeze_remote_manager as get_breeze_remote_manager
from _typeshed import Incomplete
from aioswitcher.api import SwitcherBaseResponse as SwitcherBaseResponse, SwitcherType2Api
from aioswitcher.api.remotes import SwitcherBreezeRemote as SwitcherBreezeRemote
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass
class SwitcherThermostatButtonDescriptionMixin:
    press_fn: Callable[[SwitcherType2Api, SwitcherBreezeRemote], SwitcherBaseResponse]
    supported: Callable[[SwitcherBreezeRemote], bool]
    def __init__(self, press_fn, supported) -> None: ...

@dataclass
class SwitcherThermostatButtonEntityDescription(ButtonEntityDescription, SwitcherThermostatButtonDescriptionMixin):
    def __init__(self, press_fn, supported, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

THERMOSTAT_BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherThermostatButtonEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], ButtonEntity):
    entity_description: SwitcherThermostatButtonEntityDescription
    _attr_has_entity_name: bool
    _remote: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, description: SwitcherThermostatButtonEntityDescription, remote: SwitcherBreezeRemote) -> None: ...
    async def async_press(self) -> None: ...
