from .const import ATTR_RSSI as ATTR_RSSI, DOMAIN as DOMAIN
from .coordinator import LIFXSensorUpdateCoordinator as LIFXSensorUpdateCoordinator, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXSensorEntity as LIFXSensorEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SCAN_INTERVAL: Incomplete
RSSI_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXRssiSensor(LIFXSensorEntity, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: LIFXSensorUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
