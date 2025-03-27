from . import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bosch_alarm_mode2 import Panel as Panel
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: BoschAlarmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AreaAlarmControlPanel(AlarmControlPanelEntity):
    _attr_has_entity_name: bool
    _attr_supported_features: Incomplete
    _attr_code_arm_required: bool
    _attr_name: Incomplete
    panel: Incomplete
    _area: Incomplete
    _area_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, panel: Panel, area_id: int, unique_id: str) -> None: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
