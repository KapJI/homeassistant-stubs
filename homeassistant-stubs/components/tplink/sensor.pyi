from . import legacy_device_id as legacy_device_id
from .const import ATTR_CURRENT_A as ATTR_CURRENT_A, ATTR_CURRENT_POWER_W as ATTR_CURRENT_POWER_W, ATTR_TODAY_ENERGY_KWH as ATTR_TODAY_ENERGY_KWH, ATTR_TOTAL_ENERGY_KWH as ATTR_TOTAL_ENERGY_KWH, DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_VOLTAGE as ATTR_VOLTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import SmartDevice as SmartDevice

class TPLinkSensorEntityDescription(SensorEntityDescription):
    emeter_attr: str | None
    precision: int | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, emeter_attr, precision) -> None: ...

ENERGY_SENSORS: tuple[TPLinkSensorEntityDescription, ...]

def async_emeter_from_device(device: SmartDevice, description: TPLinkSensorEntityDescription) -> float | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmartPlugSensor(CoordinatedTPLinkEntity, SensorEntity):
    entity_description: TPLinkSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkSensorEntityDescription) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float | None: ...
