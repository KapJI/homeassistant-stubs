from . import GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_AQI as ATTR_AQI, ATTR_C6H6 as ATTR_C6H6, ATTR_CO as ATTR_CO, ATTR_NO2 as ATTR_NO2, ATTR_O3 as ATTR_O3, ATTR_PM10 as ATTR_PM10, ATTR_PM25 as ATTR_PM25, ATTR_SO2 as ATTR_SO2, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, URL as URL
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from gios.model import GiosSensors as GiosSensors
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

class GiosSensorRequiredKeysMixin:
    value: Callable[[GiosSensors], StateType]
    def __init__(self, value) -> None: ...

class GiosSensorEntityDescription(SensorEntityDescription, GiosSensorRequiredKeysMixin):
    subkey: str | None
    def __init__(self, value, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, subkey) -> None: ...

SENSOR_TYPES: tuple[GiosSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GiosSensor(CoordinatorEntity[GiosDataUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: GiosSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: GiosDataUpdateCoordinator, description: GiosSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
