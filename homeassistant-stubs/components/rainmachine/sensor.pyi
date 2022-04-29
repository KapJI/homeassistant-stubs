from . import RainMachineEntity as RainMachineEntity
from .const import DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN, RUN_STATE_MAP as RUN_STATE_MAP, RunStates as RunStates
from .model import RainMachineDescriptionMixinApiCategory as RainMachineDescriptionMixinApiCategory, RainMachineDescriptionMixinUid as RainMachineDescriptionMixinUid
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow

DEFAULT_ZONE_COMPLETION_TIME_WOBBLE_TOLERANCE: Incomplete
TYPE_FLOW_SENSOR_CLICK_M3: str
TYPE_FLOW_SENSOR_CONSUMED_LITERS: str
TYPE_FLOW_SENSOR_START_INDEX: str
TYPE_FLOW_SENSOR_WATERING_CLICKS: str
TYPE_FREEZE_TEMP: str
TYPE_ZONE_RUN_COMPLETION_TIME: str

class RainMachineSensorDescriptionApiCategory(SensorEntityDescription, RainMachineDescriptionMixinApiCategory):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

class RainMachineSensorDescriptionUid(SensorEntityDescription, RainMachineDescriptionMixinUid):
    def __init__(self, uid, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProvisionSettingsSensor(RainMachineEntity, SensorEntity):
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class UniversalRestrictionsSensor(RainMachineEntity, SensorEntity):
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class ZoneTimeRemainingSensor(RainMachineEntity, SensorEntity):
    entity_description: RainMachineSensorDescriptionUid
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...
