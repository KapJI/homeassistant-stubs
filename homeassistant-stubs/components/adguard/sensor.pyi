from .const import DATA_ADGUARD_CLIENT as DATA_ADGUARD_CLIENT, DATA_ADGUARD_VERSION as DATA_ADGUARD_VERSION, DOMAIN as DOMAIN
from .entity import AdGuardHomeEntity as AdGuardHomeEntity
from _typeshed import Incomplete
from adguardhome import AdGuardHome as AdGuardHome
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TIME_MILLISECONDS as TIME_MILLISECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

class AdGuardHomeEntityDescriptionMixin:
    value_fn: Callable[[AdGuardHome], Coroutine[Any, Any, Union[int, float]]]
    def __init__(self, value_fn) -> None: ...

class AdGuardHomeEntityDescription(SensorEntityDescription, AdGuardHomeEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[AdGuardHomeEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdGuardHomeSensor(AdGuardHomeEntity, SensorEntity):
    entity_description: AdGuardHomeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry, description: AdGuardHomeEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    async def _adguard_update(self) -> None: ...
