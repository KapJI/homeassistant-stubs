from .const import DOMAIN as DOMAIN, SERVICE_TYPE_DEVICE_NAMES as SERVICE_TYPE_DEVICE_NAMES
from .coordinator import EnergyZeroData as EnergyZeroData, EnergyZeroDataUpdateCoordinator as EnergyZeroDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class EnergyZeroSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnergyZeroData], float | datetime | None]
    service_type: str
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, service_type) -> None: ...

SENSORS: tuple[EnergyZeroSensorEntityDescription, ...]

def get_gas_price(data: EnergyZeroData, hours: int) -> float | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnergyZeroSensorEntity(CoordinatorEntity[EnergyZeroDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_attribution: str
    entity_description: EnergyZeroSensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: EnergyZeroDataUpdateCoordinator, description: EnergyZeroSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | datetime | None: ...
