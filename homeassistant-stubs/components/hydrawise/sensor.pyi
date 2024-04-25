from .const import DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise.schema import Zone as Zone

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_KEYS: list[str]
TWO_YEAR_SECONDS: Incomplete
WATERING_TIME_ICON: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSensor(HydrawiseEntity, SensorEntity):
    zone: Zone
    _attr_native_value: Incomplete
    def _update_attrs(self) -> None: ...
