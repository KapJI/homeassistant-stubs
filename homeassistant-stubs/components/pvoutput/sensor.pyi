from .const import CONF_SYSTEM_ID as CONF_SYSTEM_ID, DOMAIN as DOMAIN
from .coordinator import PVOutputDataUpdateCoordinator as PVOutputDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, POWER_KILO_WATT as POWER_KILO_WATT, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pvo import Status as Status, System as System
from typing import Any

class PVOutputSensorEntityDescriptionMixin:
    value_fn: Callable[[Status], Union[int, float, None]]
    def __init__(self, value_fn) -> None: ...

class PVOutputSensorEntityDescription(SensorEntityDescription, PVOutputSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[PVOutputSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PVOutputSensorEntity(CoordinatorEntity[PVOutputDataUpdateCoordinator], SensorEntity):
    entity_description: PVOutputSensorEntityDescription
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, *, coordinator: PVOutputDataUpdateCoordinator, description: PVOutputSensorEntityDescription, system_id: str, system: System) -> None: ...
    @property
    def native_value(self) -> Union[int, float, None]: ...
