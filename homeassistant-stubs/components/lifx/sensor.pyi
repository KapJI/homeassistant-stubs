from .const import ATTR_RSSI as ATTR_RSSI
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

SCAN_INTERVAL: Incomplete
RSSI_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXRssiSensor(LIFXEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
