from .const import DOMAIN as DOMAIN, SENSORS as SENSORS
from .models import ForecastSolarSensorEntityDescription as ForecastSolarSensorEntityDescription
from datetime import datetime
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ForecastSolarSensorEntity(CoordinatorEntity, SensorEntity):
    entity_description: ForecastSolarSensorEntityDescription
    entity_id: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, *, entry_id: str, coordinator: DataUpdateCoordinator, entity_description: ForecastSolarSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[datetime, StateType]: ...
