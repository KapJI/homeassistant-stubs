from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from hydrawiser.core import Hydrawiser as Hydrawiser

BINARY_SENSOR_STATUS: Incomplete
BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]
BINARY_SENSOR_KEYS: list[str]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class HydrawiseBinarySensor(HydrawiseEntity, BinarySensorEntity):
    _attr_is_on: Incomplete
    def _handle_coordinator_update(self) -> None: ...
