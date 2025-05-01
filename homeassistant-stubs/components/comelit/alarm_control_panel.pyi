from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitVedoSystem as ComelitVedoSystem
from _typeshed import Incomplete
from aiocomelit.api import ComelitVedoAreaObject as ComelitVedoAreaObject
from aiocomelit.const import AlarmAreaState
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
_LOGGER: Incomplete
AWAY: str
DISABLE: str
HOME: str
HOME_P1: str
HOME_P2: str
NIGHT: str
ALARM_ACTIONS: dict[str, str]
ALARM_AREA_ARMED_STATUS: dict[str, int]

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitAlarmEntity(CoordinatorEntity[ComelitVedoSystem], AlarmControlPanelEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: bool
    _attr_supported_features: Incomplete
    _area_index: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ComelitVedoSystem, area: ComelitVedoAreaObject, config_entry_entry_id: str) -> None: ...
    @property
    def _area(self) -> ComelitVedoAreaObject: ...
    @property
    def available(self) -> bool: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    async def _async_update_state(self, area_state: AlarmAreaState, armed: int) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
