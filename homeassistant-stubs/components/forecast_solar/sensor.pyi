from .const import DOMAIN as DOMAIN, SENSORS as SENSORS
from .coordinator import ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from .models import ForecastSolarSensorEntityDescription as ForecastSolarSensorEntityDescription
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ForecastSolarSensorEntity(CoordinatorEntity[ForecastSolarDataUpdateCoordinator], SensorEntity):
    entity_description: ForecastSolarSensorEntityDescription
    _attr_has_entity_name: bool
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry_id: str, coordinator: ForecastSolarDataUpdateCoordinator, entity_description: ForecastSolarSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[datetime, StateType]: ...
