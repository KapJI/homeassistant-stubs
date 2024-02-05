from .const import ACCOUNT_COORDINATOR as ACCOUNT_COORDINATOR, ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN, HOP_COORDINATOR as HOP_COORDINATOR
from .coordinator import ElectricKiwiAccountDataCoordinator as ElectricKiwiAccountDataCoordinator, ElectricKiwiHOPDataCoordinator as ElectricKiwiHOPDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from electrickiwi_api.model import AccountBalance as AccountBalance, Hop as Hop
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CURRENCY_DOLLAR as CURRENCY_DOLLAR, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTR_EK_HOP_START: str
ATTR_EK_HOP_END: str
ATTR_TOTAL_RUNNING_BALANCE: str
ATTR_TOTAL_CURRENT_BALANCE: str
ATTR_NEXT_BILLING_DATE: str
ATTR_HOP_PERCENTAGE: str

@dataclass(frozen=True)
class ElectricKiwiAccountRequiredKeysMixin:
    value_func: Callable[[AccountBalance], float | datetime]
    def __init__(self, value_func) -> None: ...

@dataclass(frozen=True)
class ElectricKiwiAccountSensorEntityDescription(SensorEntityDescription, ElectricKiwiAccountRequiredKeysMixin):
    def __init__(self, value_func, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

ACCOUNT_SENSOR_TYPES: tuple[ElectricKiwiAccountSensorEntityDescription, ...]

@dataclass(frozen=True)
class ElectricKiwiHOPRequiredKeysMixin:
    value_func: Callable[[Hop], datetime]
    def __init__(self, value_func) -> None: ...

@dataclass(frozen=True)
class ElectricKiwiHOPSensorEntityDescription(SensorEntityDescription, ElectricKiwiHOPRequiredKeysMixin):
    def __init__(self, value_func, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

def _check_and_move_time(hop: Hop, time: str) -> datetime: ...

HOP_SENSOR_TYPES: tuple[ElectricKiwiHOPSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElectricKiwiAccountEntity(CoordinatorEntity[ElectricKiwiAccountDataCoordinator], SensorEntity):
    entity_description: ElectricKiwiAccountSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElectricKiwiAccountDataCoordinator, description: ElectricKiwiAccountSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | datetime: ...

class ElectricKiwiHOPEntity(CoordinatorEntity[ElectricKiwiHOPDataCoordinator], SensorEntity):
    entity_description: ElectricKiwiHOPSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElectricKiwiHOPDataCoordinator, description: ElectricKiwiHOPSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime: ...
