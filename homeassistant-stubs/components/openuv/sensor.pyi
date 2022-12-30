from . import OpenUvEntity as OpenUvEntity
from .const import DATA_UV as DATA_UV, DOMAIN as DOMAIN, TYPE_CURRENT_OZONE_LEVEL as TYPE_CURRENT_OZONE_LEVEL, TYPE_CURRENT_UV_INDEX as TYPE_CURRENT_UV_INDEX, TYPE_CURRENT_UV_LEVEL as TYPE_CURRENT_UV_LEVEL, TYPE_MAX_UV_INDEX as TYPE_MAX_UV_INDEX, TYPE_SAFE_EXPOSURE_TIME_1 as TYPE_SAFE_EXPOSURE_TIME_1, TYPE_SAFE_EXPOSURE_TIME_2 as TYPE_SAFE_EXPOSURE_TIME_2, TYPE_SAFE_EXPOSURE_TIME_3 as TYPE_SAFE_EXPOSURE_TIME_3, TYPE_SAFE_EXPOSURE_TIME_4 as TYPE_SAFE_EXPOSURE_TIME_4, TYPE_SAFE_EXPOSURE_TIME_5 as TYPE_SAFE_EXPOSURE_TIME_5, TYPE_SAFE_EXPOSURE_TIME_6 as TYPE_SAFE_EXPOSURE_TIME_6
from .coordinator import OpenUvCoordinator as OpenUvCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UV_INDEX as UV_INDEX, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import as_local as as_local, parse_datetime as parse_datetime

ATTR_MAX_UV_TIME: str
EXPOSURE_TYPE_MAP: Incomplete
UV_LEVEL_EXTREME: str
UV_LEVEL_VHIGH: str
UV_LEVEL_HIGH: str
UV_LEVEL_MODERATE: str
UV_LEVEL_LOW: str
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenUvSensor(OpenUvEntity, SensorEntity):
    _attr_native_value: Incomplete
    def _update_from_latest_data(self) -> None: ...
