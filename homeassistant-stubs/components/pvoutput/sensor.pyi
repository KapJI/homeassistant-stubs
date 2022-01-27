from .const import ATTR_EFFICIENCY as ATTR_EFFICIENCY, ATTR_ENERGY_CONSUMPTION as ATTR_ENERGY_CONSUMPTION, ATTR_ENERGY_GENERATION as ATTR_ENERGY_GENERATION, ATTR_POWER_CONSUMPTION as ATTR_POWER_CONSUMPTION, ATTR_POWER_GENERATION as ATTR_POWER_GENERATION, CONF_SYSTEM_ID as CONF_SYSTEM_ID, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import PVOutputDataUpdateCoordinator as PVOutputDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_VOLTAGE as ATTR_VOLTAGE, CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, POWER_KILO_WATT as POWER_KILO_WATT, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pvo import Status as Status, System as System
from typing import Any

class PVOutputSensorEntityDescriptionMixin:
    value_fn: Callable[[Status], Union[int, float, None]]
    def __init__(self, value_fn) -> None: ...

class PVOutputSensorEntityDescription(SensorEntityDescription, PVOutputSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[PVOutputSensorEntityDescription, ...]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PVOutputSensorEntity(CoordinatorEntity, SensorEntity):
    coordinator: PVOutputDataUpdateCoordinator
    entity_description: PVOutputSensorEntityDescription
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: PVOutputDataUpdateCoordinator, description: PVOutputSensorEntityDescription, system_id: str, system: System) -> None: ...
    @property
    def native_value(self) -> Union[int, float, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Union[int, float, None]], None]: ...
