from . import OpenUvEntity as OpenUvEntity
from .const import DATA_UV as DATA_UV, DOMAIN as DOMAIN, TYPE_CURRENT_OZONE_LEVEL as TYPE_CURRENT_OZONE_LEVEL, TYPE_CURRENT_UV_INDEX as TYPE_CURRENT_UV_INDEX, TYPE_CURRENT_UV_LEVEL as TYPE_CURRENT_UV_LEVEL, TYPE_MAX_UV_INDEX as TYPE_MAX_UV_INDEX, TYPE_SAFE_EXPOSURE_TIME_1 as TYPE_SAFE_EXPOSURE_TIME_1, TYPE_SAFE_EXPOSURE_TIME_2 as TYPE_SAFE_EXPOSURE_TIME_2, TYPE_SAFE_EXPOSURE_TIME_3 as TYPE_SAFE_EXPOSURE_TIME_3, TYPE_SAFE_EXPOSURE_TIME_4 as TYPE_SAFE_EXPOSURE_TIME_4, TYPE_SAFE_EXPOSURE_TIME_5 as TYPE_SAFE_EXPOSURE_TIME_5, TYPE_SAFE_EXPOSURE_TIME_6 as TYPE_SAFE_EXPOSURE_TIME_6
from .coordinator import OpenUvCoordinator as OpenUvCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UV_INDEX as UV_INDEX, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import as_local as as_local, parse_datetime as parse_datetime
from typing import Any

ATTR_MAX_UV_TIME: str
EXPOSURE_TYPE_MAP: Incomplete

@dataclass
class UvLabel:
    value: str
    minimum_index: int
    def __init__(self, value, minimum_index) -> None: ...

UV_LABEL_DEFINITIONS: Incomplete

def get_uv_label(uv_index: int) -> str: ...

@dataclass(frozen=True, kw_only=True)
class OpenUvSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], int | str]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenUvSensor(OpenUvEntity, SensorEntity):
    entity_description: OpenUvSensorEntityDescription
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def native_value(self) -> int | str: ...
