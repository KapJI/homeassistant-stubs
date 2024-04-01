from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyenphase import EnvoyEncharge as EnvoyEncharge, EnvoyEnpower as EnvoyEnpower

@dataclass(frozen=True, kw_only=True)
class EnvoyEnchargeBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyEncharge], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

ENCHARGE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyEnpowerBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyEnpower], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

ENPOWER_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnvoyBaseBinarySensorEntity(EnvoyBaseEntity, BinarySensorEntity): ...

class EnvoyEnchargeBinarySensorEntity(EnvoyBaseBinarySensorEntity):
    entity_description: EnvoyEnchargeBinarySensorEntityDescription
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnchargeBinarySensorEntityDescription, serial_number: str) -> None: ...
    @property
    def is_on(self) -> bool: ...

class EnvoyEnpowerBinarySensorEntity(EnvoyBaseBinarySensorEntity):
    entity_description: EnvoyEnpowerBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnpowerBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
