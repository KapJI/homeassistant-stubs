from . import GhostConfigEntry as GhostConfigEntry
from .const import CURRENCY as CURRENCY, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL
from .coordinator import GhostData as GhostData, GhostDataUpdateCoordinator as GhostDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

def _get_currency_value(currency_data: dict[str, Any]) -> int | None: ...

@dataclass(frozen=True, kw_only=True)
class GhostSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GhostData], str | int | None]

SENSORS: tuple[GhostSensorEntityDescription, ...]
REVENUE_SENSORS: tuple[GhostSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GhostConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GhostSensorEntity(CoordinatorEntity[GhostDataUpdateCoordinator], SensorEntity):
    entity_description: GhostSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GhostDataUpdateCoordinator, description: GhostSensorEntityDescription, entry: GhostConfigEntry) -> None: ...
    @property
    def native_value(self) -> str | int | None: ...

class GhostNewsletterSensorEntity(CoordinatorEntity[GhostDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_state_class: Incomplete
    _newsletter_id: Incomplete
    _newsletter_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GhostDataUpdateCoordinator, entry: GhostConfigEntry, newsletter_id: str, newsletter_name: str) -> None: ...
    def _get_newsletter_by_id(self) -> dict[str, Any] | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int | None: ...
