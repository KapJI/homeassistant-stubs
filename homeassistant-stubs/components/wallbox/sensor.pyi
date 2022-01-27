from . import WallboxCoordinator as WallboxCoordinator, WallboxEntity as WallboxEntity
from .const import CONF_ADDED_ENERGY_KEY as CONF_ADDED_ENERGY_KEY, CONF_ADDED_RANGE_KEY as CONF_ADDED_RANGE_KEY, CONF_CHARGING_POWER_KEY as CONF_CHARGING_POWER_KEY, CONF_CHARGING_SPEED_KEY as CONF_CHARGING_SPEED_KEY, CONF_COST_KEY as CONF_COST_KEY, CONF_CURRENT_MODE_KEY as CONF_CURRENT_MODE_KEY, CONF_DATA_KEY as CONF_DATA_KEY, CONF_DEPOT_PRICE_KEY as CONF_DEPOT_PRICE_KEY, CONF_MAX_AVAILABLE_POWER_KEY as CONF_MAX_AVAILABLE_POWER_KEY, CONF_MAX_CHARGING_CURRENT_KEY as CONF_MAX_CHARGING_CURRENT_KEY, CONF_SERIAL_NUMBER_KEY as CONF_SERIAL_NUMBER_KEY, CONF_STATE_OF_CHARGE_KEY as CONF_STATE_OF_CHARGE_KEY, CONF_STATUS_DESCRIPTION_KEY as CONF_STATUS_DESCRIPTION_KEY, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

CONF_STATION: str
UPDATE_INTERVAL: int
_LOGGER: Any

class WallboxSensorEntityDescription(SensorEntityDescription):
    precision: Union[int, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, precision) -> None: ...

SENSOR_TYPES: dict[str, WallboxSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxSensor(WallboxEntity, SensorEntity):
    entity_description: WallboxSensorEntityDescription
    coordinator: WallboxCoordinator
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
