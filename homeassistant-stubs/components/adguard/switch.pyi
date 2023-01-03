from .const import DATA_ADGUARD_CLIENT as DATA_ADGUARD_CLIENT, DATA_ADGUARD_VERSION as DATA_ADGUARD_VERSION, DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import AdGuardHomeEntity as AdGuardHomeEntity
from _typeshed import Incomplete
from adguardhome import AdGuardHome as AdGuardHome
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

class AdGuardHomeSwitchEntityDescriptionMixin:
    is_on_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, bool]]]
    turn_on_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, None]]]
    turn_off_fn: Callable[[AdGuardHome], Callable[[], Coroutine[Any, Any, None]]]
    def __init__(self, is_on_fn, turn_on_fn, turn_off_fn) -> None: ...

class AdGuardHomeSwitchEntityDescription(SwitchEntityDescription, AdGuardHomeSwitchEntityDescriptionMixin):
    def __init__(self, is_on_fn, turn_on_fn, turn_off_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCHES: tuple[AdGuardHomeSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdGuardHomeSwitch(AdGuardHomeEntity, SwitchEntity):
    entity_description: AdGuardHomeSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry, description: AdGuardHomeSwitchEntityDescription) -> None: ...
    _attr_available: bool
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    async def _adguard_update(self) -> None: ...
