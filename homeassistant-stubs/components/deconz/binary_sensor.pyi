from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.interfaces.sensors import SensorResources as SensorResources
from pydeconz.models.event import EventType as EventType

ATTR_ORIENTATION: str
ATTR_TILTANGLE: str
ATTR_VIBRATIONSTRENGTH: str
PROVIDES_EXTRA_ATTRIBUTES: Incomplete

class DeconzBinarySensorDescriptionMixin:
    suffix: str
    update_key: str
    value_fn: Callable[[SensorResources], Union[bool, None]]
    def __init__(self, suffix, update_key, value_fn) -> None: ...

class DeconzBinarySensorDescription(BinarySensorEntityDescription, DeconzBinarySensorDescriptionMixin):
    def __init__(self, suffix, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete
BINARY_SENSOR_DESCRIPTIONS: Incomplete

def async_update_unique_id(hass: HomeAssistant, unique_id: str, description: DeconzBinarySensorDescription) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBinarySensor(DeconzDevice, BinarySensorEntity):
    TYPE: Incomplete
    _device: SensorResources
    entity_description: DeconzBinarySensorDescription
    _attr_name: Incomplete
    _update_keys: Incomplete
    def __init__(self, device: SensorResources, gateway: DeconzGateway, description: DeconzBinarySensorDescription) -> None: ...
    @property
    def unique_id(self) -> str: ...
    def async_update_callback(self) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[bool, float, int, list, None]]: ...
