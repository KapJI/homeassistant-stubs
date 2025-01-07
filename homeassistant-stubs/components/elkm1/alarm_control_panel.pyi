from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .const import ATTR_CHANGED_BY_ID as ATTR_CHANGED_BY_ID, ATTR_CHANGED_BY_KEYPAD as ATTR_CHANGED_BY_KEYPAD, ATTR_CHANGED_BY_TIME as ATTR_CHANGED_BY_TIME, ELK_USER_CODE_SERVICE_SCHEMA as ELK_USER_CODE_SERVICE_SCHEMA
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.areas import Area as Area
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from homeassistant.components.alarm_control_panel import ATTR_CHANGED_BY as ATTR_CHANGED_BY, AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

DISPLAY_MESSAGE_SERVICE_SCHEMA: VolDictType
SERVICE_ALARM_DISPLAY_MESSAGE: str
SERVICE_ALARM_ARM_VACATION: str
SERVICE_ALARM_ARM_HOME_INSTANT: str
SERVICE_ALARM_ARM_NIGHT_INSTANT: str
SERVICE_ALARM_BYPASS: str
SERVICE_ALARM_CLEAR_BYPASS: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkArea(ElkAttachedEntity, AlarmControlPanelEntity, RestoreEntity):
    _attr_supported_features: Incomplete
    _element: Area
    _elk: Incomplete
    _changed_by_keypad: str | None
    _changed_by_time: str | None
    _changed_by_id: int | None
    _changed_by: str | None
    _state: AlarmControlPanelState | None
    def __init__(self, element: Element, elk: Elk, elk_data: ELKM1Data) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _watch_keypad(self, keypad: Element, changeset: dict[str, Any]) -> None: ...
    def _watch_area(self, area: Element, changeset: dict[str, Any]) -> None: ...
    @property
    def code_format(self) -> CodeFormat | None: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def changed_by(self) -> str | None: ...
    def _element_changed(self, element: Element, changeset: dict[str, Any]) -> None: ...
    def _entry_exit_timer_is_running(self) -> bool: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home_instant(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night_instant(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_display_message(self, clear: int, beep: bool, timeout: int, line1: str, line2: str) -> None: ...
    async def async_bypass(self, code: str | None = None) -> None: ...
    async def async_clear_bypass(self, code: str | None = None) -> None: ...
