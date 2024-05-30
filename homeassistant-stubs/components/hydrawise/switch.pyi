from .const import DEFAULT_WATERING_TIME as DEFAULT_WATERING_TIME, DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise import Hydrawise as Hydrawise, Zone as Zone
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HydrawiseSwitchEntityDescription(SwitchEntityDescription):
    turn_on_fn: Callable[[Hydrawise, Zone], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[Hydrawise, Zone], Coroutine[Any, Any, None]]
    value_fn: Callable[[Zone], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, turn_on_fn, turn_off_fn, value_fn) -> None: ...

SWITCH_TYPES: tuple[HydrawiseSwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSwitch(HydrawiseEntity, SwitchEntity):
    entity_description: HydrawiseSwitchEntityDescription
    zone: Zone
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_attrs(self) -> None: ...
