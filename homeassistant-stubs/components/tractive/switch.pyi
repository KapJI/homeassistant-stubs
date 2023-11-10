from . import Trackables as Trackables, TractiveClient as TractiveClient
from .const import ATTR_BUZZER as ATTR_BUZZER, ATTR_LED as ATTR_LED, ATTR_LIVE_TRACKING as ATTR_LIVE_TRACKING, CLIENT as CLIENT, DOMAIN as DOMAIN, TRACKABLES as TRACKABLES, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

_LOGGER: Incomplete

@dataclass
class TractiveRequiredKeysMixin:
    method: Literal['async_set_buzzer', 'async_set_led', 'async_set_live_tracking']
    def __init__(self, method) -> None: ...

@dataclass
class TractiveSwitchEntityDescription(SwitchEntityDescription, TractiveRequiredKeysMixin):
    def __init__(self, method, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCH_TYPES: tuple[TractiveSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TractiveSwitch(TractiveEntity, SwitchEntity):
    entity_description: TractiveSwitchEntityDescription
    _attr_unique_id: Incomplete
    _attr_available: bool
    _tracker: Incomplete
    _method: Incomplete
    def __init__(self, client: TractiveClient, item: Trackables, description: TractiveSwitchEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def handle_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_buzzer(self, active: bool) -> dict[str, Any]: ...
    async def async_set_led(self, active: bool) -> dict[str, Any]: ...
    async def async_set_live_tracking(self, active: bool) -> dict[str, Any]: ...
