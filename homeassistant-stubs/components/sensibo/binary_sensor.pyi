from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, SensiboMotionBaseEntity as SensiboMotionBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import MotionSensor as MotionSensor, SensiboDevice as SensiboDevice

PARALLEL_UPDATES: int

class MotionBaseEntityDescriptionMixin:
    value_fn: Callable[[MotionSensor], Union[bool, None]]
    def __init__(self, value_fn) -> None: ...

class DeviceBaseEntityDescriptionMixin:
    value_fn: Callable[[SensiboDevice], Union[bool, None]]
    def __init__(self, value_fn) -> None: ...

class SensiboMotionBinarySensorEntityDescription(BinarySensorEntityDescription, MotionBaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class SensiboDeviceBinarySensorEntityDescription(BinarySensorEntityDescription, DeviceBaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

FILTER_CLEAN_REQUIRED_DESCRIPTION: Incomplete
MOTION_SENSOR_TYPES: tuple[SensiboMotionBinarySensorEntityDescription, ...]
MOTION_DEVICE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
DEVICE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
PURE_SENSOR_TYPES: tuple[SensiboDeviceBinarySensorEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboMotionSensor(SensiboMotionBaseEntity, BinarySensorEntity):
    entity_description: SensiboMotionBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, sensor_id: str, sensor_data: MotionSensor, entity_description: SensiboMotionBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class SensiboDeviceSensor(SensiboDeviceBaseEntity, BinarySensorEntity):
    entity_description: SensiboDeviceBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
