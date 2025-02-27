from .const import CONF_REMOTE_ACCESS_ENABLED as CONF_REMOTE_ACCESS_ENABLED, CONF_REMOTE_ACCESS_HOST as CONF_REMOTE_ACCESS_HOST, CONF_REMOTE_ACCESS_PORT as CONF_REMOTE_ACCESS_PORT
from .coordinator import FluxLedConfigEntry as FluxLedConfigEntry, FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .discovery import async_clear_discovery_cache as async_clear_discovery_cache
from .entity import FluxBaseEntity as FluxBaseEntity, FluxEntity as FluxEntity, FluxOnOffEntity as FluxOnOffEntity
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: FluxLedConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FluxSwitch(FluxOnOffEntity, CoordinatorEntity[FluxLedUpdateCoordinator], SwitchEntity):
    _attr_name: Incomplete
    async def _async_turn_on(self, **kwargs: Any) -> None: ...

class FluxRemoteAccessSwitch(FluxBaseEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, device: AIOWifiLedBulb, entry: FluxLedConfigEntry) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def _async_update_entry(self, new_state: bool) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class FluxMusicSwitch(FluxEntity, SwitchEntity):
    _attr_translation_key: str
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
