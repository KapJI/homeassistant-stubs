from .const import DOMAIN as DOMAIN
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fullykiosk import FullyKiosk as FullyKiosk
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass
class FullySwitchEntityDescriptionMixin:
    on_action: Callable[[FullyKiosk], Any]
    off_action: Callable[[FullyKiosk], Any]
    is_on_fn: Callable[[dict[str, Any]], Any]
    mqtt_on_event: str | None
    mqtt_off_event: str | None
    def __init__(self, on_action, off_action, is_on_fn, mqtt_on_event, mqtt_off_event) -> None: ...

@dataclass
class FullySwitchEntityDescription(SwitchEntityDescription, FullySwitchEntityDescriptionMixin):
    def __init__(self, on_action, off_action, is_on_fn, mqtt_on_event, mqtt_off_event, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCHES: tuple[FullySwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullySwitchEntity(FullyKioskEntity, SwitchEntity):
    entity_description: FullySwitchEntityDescription
    _attr_unique_id: Incomplete
    _turned_on_subscription: Incomplete
    _turned_off_subscription: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator, description: FullySwitchEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: bool
    def _turn_off(self, **kwargs: Any) -> None: ...
    def _turn_on(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
