from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry, EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyenphase import Envoy as Envoy, EnvoyDryContactSettings as EnvoyDryContactSettings
from pyenphase.models.tariff import EnvoyStorageSettings as EnvoyStorageSettings
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EnvoyRelayNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[EnvoyDryContactSettings], float]

@dataclass(frozen=True, kw_only=True)
class EnvoyStorageSettingsNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[EnvoyStorageSettings], float]
    update_fn: Callable[[Envoy, float], Awaitable[dict[str, Any]]]

RELAY_ENTITIES: Incomplete
STORAGE_RESERVE_SOC_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EnphaseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EnvoyRelayNumberEntity(EnvoyBaseEntity, NumberEntity):
    entity_description: EnvoyRelayNumberEntityDescription
    envoy: Incomplete
    _relay_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyRelayNumberEntityDescription, relay_id: str) -> None: ...
    @property
    def native_value(self) -> float: ...
    @exception_handler
    async def async_set_native_value(self, value: float) -> None: ...

class EnvoyStorageSettingsNumberEntity(EnvoyBaseEntity, NumberEntity):
    entity_description: EnvoyStorageSettingsNumberEntityDescription
    envoy: Incomplete
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyStorageSettingsNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
