from . import TautulliEntity as TautulliEntity
from .const import ATTR_TOP_USER as ATTR_TOP_USER, DOMAIN as DOMAIN
from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import DATA_KILOBITS as DATA_KILOBITS, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from pytautulli import PyTautulliApiActivity as PyTautulliApiActivity, PyTautulliApiHomeStats as PyTautulliApiHomeStats, PyTautulliApiSession as PyTautulliApiSession, PyTautulliApiUser as PyTautulliApiUser

def get_top_stats(home_stats: PyTautulliApiHomeStats, activity: PyTautulliApiActivity, key: str) -> Union[str, None]: ...

class TautulliSensorEntityMixin:
    value_fn: Callable[[PyTautulliApiHomeStats, PyTautulliApiActivity, str], StateType]
    def __init__(self, value_fn) -> None: ...

class TautulliSensorEntityDescription(SensorEntityDescription, TautulliSensorEntityMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: tuple[TautulliSensorEntityDescription, ...]

class TautulliSessionSensorEntityMixin:
    value_fn: Callable[[PyTautulliApiSession], StateType]
    def __init__(self, value_fn) -> None: ...

class TautulliSessionSensorEntityDescription(SensorEntityDescription, TautulliSessionSensorEntityMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SESSION_SENSOR_TYPES: tuple[TautulliSessionSensorEntityDescription, ...]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TautulliSensor(TautulliEntity, SensorEntity):
    entity_description: TautulliSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class TautulliSessionSensor(TautulliEntity, SensorEntity):
    entity_description: TautulliSessionSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TautulliDataUpdateCoordinator, description: EntityDescription, user: PyTautulliApiUser) -> None: ...
    @property
    def native_value(self) -> StateType: ...
