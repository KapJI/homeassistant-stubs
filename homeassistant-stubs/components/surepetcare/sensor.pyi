from . import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .const import DOMAIN as DOMAIN, SURE_BATT_VOLTAGE_DIFF as SURE_BATT_VOLTAGE_DIFF, SURE_BATT_VOLTAGE_LOW as SURE_BATT_VOLTAGE_LOW
from .entity import SurePetcareEntity as SurePetcareEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_VOLTAGE as ATTR_VOLTAGE, PERCENTAGE as PERCENTAGE, VOLUME_MILLILITERS as VOLUME_MILLILITERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from surepy.entities import SurepyEntity as SurepyEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SureBattery(SurePetcareEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...

class Felaqua(SurePetcareEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_picture: Incomplete
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    _attr_native_value: Incomplete
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
