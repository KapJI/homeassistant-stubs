from .const import CONF_ADDED_ENERGY_KEY as CONF_ADDED_ENERGY_KEY, CONF_ADDED_RANGE_KEY as CONF_ADDED_RANGE_KEY, CONF_CHARGING_POWER_KEY as CONF_CHARGING_POWER_KEY, CONF_CHARGING_SPEED_KEY as CONF_CHARGING_SPEED_KEY, CONF_COST_KEY as CONF_COST_KEY, CONF_CURRENT_MODE_KEY as CONF_CURRENT_MODE_KEY, CONF_DEPOT_PRICE_KEY as CONF_DEPOT_PRICE_KEY, CONF_MAX_AVAILABLE_POWER_KEY as CONF_MAX_AVAILABLE_POWER_KEY, CONF_MAX_CHARGING_CURRENT_KEY as CONF_MAX_CHARGING_CURRENT_KEY, CONF_STATE_OF_CHARGE_KEY as CONF_STATE_OF_CHARGE_KEY, CONF_STATUS_DESCRIPTION_KEY as CONF_STATUS_DESCRIPTION_KEY, DOMAIN as DOMAIN
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.components.wallbox import WallboxCoordinator as WallboxCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

CONF_STATION: str
UPDATE_INTERVAL: int
_LOGGER: Any

class WallboxSensorEntityDescription(SensorEntityDescription):
    precision: Union[int, None]

SENSOR_TYPES: dict[str, WallboxSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxSensor(CoordinatorEntity, SensorEntity):
    entity_description: WallboxSensorEntityDescription
    coordinator: WallboxCoordinator
    _attr_name: Any
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
