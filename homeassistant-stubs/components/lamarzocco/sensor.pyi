from . import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud.lm_machine import LaMarzoccoMachine as LaMarzoccoMachine

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSensorEntityDescription(LaMarzoccoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[LaMarzoccoMachine], float | int]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., available_fn=..., supported_fn=..., value_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSensorEntity(LaMarzoccoEntity, SensorEntity):
    entity_description: LaMarzoccoSensorEntityDescription
    @property
    def native_value(self) -> int | float: ...
