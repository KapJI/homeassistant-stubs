from .coordinator import TedeeConfigEntry as TedeeConfigEntry
from .entity import TedeeDescriptionEntity as TedeeDescriptionEntity
from aiotedee import TedeeLock as TedeeLock
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TedeeBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[TedeeLock], bool | None]
    supported_fn: Callable[[TedeeLock], bool] = ...
    available_fn: Callable[[TedeeLock], bool] = ...
    always_available: bool = ...

ENTITIES: tuple[TedeeBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TedeeBinarySensorEntity(TedeeDescriptionEntity, BinarySensorEntity):
    entity_description: TedeeBinarySensorEntityDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def available(self) -> bool: ...
