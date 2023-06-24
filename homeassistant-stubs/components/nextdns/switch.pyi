from . import CoordinatorDataT as CoordinatorDataT, NextDnsSettingsUpdateCoordinator as NextDnsSettingsUpdateCoordinator
from .const import ATTR_SETTINGS as ATTR_SETTINGS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Generic

PARALLEL_UPDATES: int

class NextDnsSwitchRequiredKeysMixin(Generic[CoordinatorDataT]):
    state: Callable[[CoordinatorDataT], bool]
    def __init__(self, state) -> None: ...

class NextDnsSwitchEntityDescription(SwitchEntityDescription, NextDnsSwitchRequiredKeysMixin[CoordinatorDataT]):
    def __init__(self, state, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsSwitch(CoordinatorEntity[NextDnsSettingsUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    entity_description: NextDnsSwitchEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: NextDnsSettingsUpdateCoordinator, description: NextDnsSwitchEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_setting(self, new_state: bool) -> None: ...
