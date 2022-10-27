from . import WallboxCoordinator as WallboxCoordinator, WallboxEntity as WallboxEntity
from .const import CHARGER_ADDED_DISCHARGED_ENERGY_KEY as CHARGER_ADDED_DISCHARGED_ENERGY_KEY, CHARGER_ADDED_ENERGY_KEY as CHARGER_ADDED_ENERGY_KEY, CHARGER_ADDED_RANGE_KEY as CHARGER_ADDED_RANGE_KEY, CHARGER_CHARGING_POWER_KEY as CHARGER_CHARGING_POWER_KEY, CHARGER_CHARGING_SPEED_KEY as CHARGER_CHARGING_SPEED_KEY, CHARGER_COST_KEY as CHARGER_COST_KEY, CHARGER_CURRENT_MODE_KEY as CHARGER_CURRENT_MODE_KEY, CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_DEPOT_PRICE_KEY as CHARGER_DEPOT_PRICE_KEY, CHARGER_MAX_AVAILABLE_POWER_KEY as CHARGER_MAX_AVAILABLE_POWER_KEY, CHARGER_MAX_CHARGING_CURRENT_KEY as CHARGER_MAX_CHARGING_CURRENT_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, CHARGER_STATE_OF_CHARGE_KEY as CHARGER_STATE_OF_CHARGE_KEY, CHARGER_STATUS_DESCRIPTION_KEY as CHARGER_STATUS_DESCRIPTION_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

CHARGER_STATION: str
UPDATE_INTERVAL: int
_LOGGER: Incomplete

class WallboxSensorEntityDescription(SensorEntityDescription):
    precision: Union[int, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, precision) -> None: ...

SENSOR_TYPES: dict[str, WallboxSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxSensor(WallboxEntity, SensorEntity):
    entity_description: WallboxSensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
