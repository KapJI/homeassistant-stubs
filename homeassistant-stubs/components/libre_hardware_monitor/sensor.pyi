from . import LibreHardwareMonitorConfigEntry as LibreHardwareMonitorConfigEntry, LibreHardwareMonitorCoordinator as LibreHardwareMonitorCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from librehardwaremonitor_api.model import LibreHardwareMonitorSensorData as LibreHardwareMonitorSensorData
from typing import Any

PARALLEL_UPDATES: int
STATE_MIN_VALUE: str
STATE_MAX_VALUE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: LibreHardwareMonitorConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LibreHardwareMonitorSensor(CoordinatorEntity[LibreHardwareMonitorCoordinator], SensorEntity):
    _attr_state_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: str
    _attr_native_value: str | None
    _attr_extra_state_attributes: dict[str, Any]
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: str
    _sensor_id: str
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LibreHardwareMonitorCoordinator, entry_id: str, sensor_data: LibreHardwareMonitorSensorData) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
