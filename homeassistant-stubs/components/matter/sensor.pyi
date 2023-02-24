from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.Types import Nullable as Nullable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterSensor(MatterEntity, SensorEntity):
    _attr_state_class: Incomplete
    _attr_native_value: Incomplete
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
