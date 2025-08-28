from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry, EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyenphase import EnvoyC6CC as EnvoyC6CC, EnvoyCollar as EnvoyCollar, EnvoyEncharge as EnvoyEncharge, EnvoyEnpower as EnvoyEnpower

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EnvoyEnchargeBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyEncharge], bool]

ENCHARGE_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyEnpowerBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyEnpower], bool]

ENPOWER_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyCollarBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyCollar], bool]

COLLAR_SENSORS: Incomplete

@dataclass(frozen=True, kw_only=True)
class EnvoyC6CCBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[EnvoyC6CC], bool]

C6CC_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EnphaseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

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

class EnvoyCollarBinarySensorEntity(EnvoyBaseBinarySensorEntity):
    entity_description: EnvoyCollarBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyCollarBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class EnvoyC6CCBinarySensorEntity(EnvoyBaseBinarySensorEntity):
    entity_description: EnvoyC6CCBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyC6CCBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
