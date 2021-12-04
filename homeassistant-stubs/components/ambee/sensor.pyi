from .const import DOMAIN as DOMAIN, SENSORS as SENSORS, SERVICES as SERVICES
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbeeSensorEntity(CoordinatorEntity, SensorEntity):
    _service_key: Any
    entity_id: Any
    entity_description: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry_id: str, description: SensorEntityDescription, service_key: str, service: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
