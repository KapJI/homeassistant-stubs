from . import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from .entity import BoschAlarmAreaEntity as BoschAlarmAreaEntity, BoschAlarmEntity as BoschAlarmEntity, BoschAlarmPointEntity as BoschAlarmPointEntity
from _typeshed import Incomplete
from bosch_alarm_mode2 import Panel as Panel
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class BoschAlarmFaultEntityDescription(BinarySensorEntityDescription):
    fault: int

FAULT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: BoschAlarmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class PanelFaultsSensor(BoschAlarmEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    entity_description: BoschAlarmFaultEntityDescription
    _fault_type: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, unique_id: str, entity_description: BoschAlarmFaultEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class AreaReadyToArmSensor(BoschAlarmAreaEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    panel: Incomplete
    _arm_type: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, area_id: int, unique_id: str, arm_type: str) -> None: ...
    @property
    def is_on(self) -> bool: ...

class PointSensor(BoschAlarmPointEntity, BinarySensorEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, point_id: int, unique_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
