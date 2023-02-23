from .const import DOMAIN as DOMAIN
from .entity import PowerWallEntity as PowerWallEntity
from .models import PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tesla_powerwall import IslandMode
from typing import Any

OFF_GRID_STATUSES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerwallOffGridEnabledEntity(PowerWallEntity, SwitchEntity):
    _attr_name: str
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    async def _async_set_island_mode(self, island_mode: IslandMode) -> None: ...
