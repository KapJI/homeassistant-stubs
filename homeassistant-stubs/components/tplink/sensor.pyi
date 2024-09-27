from . import TPLinkConfigEntry as TPLinkConfigEntry
from .const import UNIT_MAPPING as UNIT_MAPPING
from .deprecate import async_cleanup_deprecated as async_cleanup_deprecated
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class TPLinkSensorEntityDescription(SensorEntityDescription, TPLinkFeatureEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., deprecated_info=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=...) -> None: ...

SENSOR_DESCRIPTIONS: tuple[TPLinkSensorEntityDescription, ...]
SENSOR_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSensorEntity(CoordinatedTPLinkFeatureEntity, SensorEntity):
    entity_description: TPLinkSensorEntityDescription
    _attr_suggested_display_precision: Incomplete
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def _async_update_attrs(self) -> None: ...
