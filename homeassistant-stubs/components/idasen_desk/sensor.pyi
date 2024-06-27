from . import DeskData as DeskData, IdasenDeskCoordinator as IdasenDeskCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class IdasenDeskSensorDescription(SensorEntityDescription):
    value_fn: Callable[[IdasenDeskCoordinator], float | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IdasenDeskSensor(CoordinatorEntity[IdasenDeskCoordinator], SensorEntity):
    entity_description: IdasenDeskSensorDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _address: Incomplete
    _desk: Incomplete
    def __init__(self, address: str, device_info: DeviceInfo, coordinator: IdasenDeskCoordinator, description: IdasenDeskSensorDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    def _handle_coordinator_update(self, *args: Any) -> None: ...
    _attr_native_value: Incomplete
    def _update_native_value(self) -> None: ...
