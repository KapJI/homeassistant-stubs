from .const import DOMAIN as DOMAIN
from .coordinator import ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from forecast_solar.models import Estimate as Estimate
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class ForecastSolarSensorEntityDescription(SensorEntityDescription):
    state: Callable[[Estimate], Any] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, state) -> None: ...

SENSORS: tuple[ForecastSolarSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ForecastSolarSensorEntity(CoordinatorEntity[ForecastSolarDataUpdateCoordinator], SensorEntity):
    entity_description: ForecastSolarSensorEntityDescription
    _attr_has_entity_name: bool
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry_id: str, coordinator: ForecastSolarDataUpdateCoordinator, entity_description: ForecastSolarSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...
