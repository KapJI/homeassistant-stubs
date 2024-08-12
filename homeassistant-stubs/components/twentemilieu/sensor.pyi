from .const import DOMAIN as DOMAIN
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from twentemilieu import WasteType

@dataclass(frozen=True, kw_only=True)
class TwenteMilieuSensorDescription(SensorEntityDescription):
    waste_type: WasteType
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., waste_type) -> None: ...

SENSORS: tuple[TwenteMilieuSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuSensor(TwenteMilieuEntity, SensorEntity):
    entity_description: TwenteMilieuSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, description: TwenteMilieuSensorDescription) -> None: ...
    @property
    def native_value(self) -> date | None: ...
