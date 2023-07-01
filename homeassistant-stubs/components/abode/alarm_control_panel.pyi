import homeassistant.components.alarm_control_panel as alarm
from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.alarm import Alarm as AbodeAl

ICON: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeAlarm(AbodeDevice, alarm.AlarmControlPanelEntity):
    _attr_icon = ICON
    _attr_name: Incomplete
    _attr_code_arm_required: bool
    _attr_supported_features: Incomplete
    _device: AbodeAl
    @property
    def state(self) -> str | None: ...
    def alarm_disarm(self, code: str | None = ...) -> None: ...
    def alarm_arm_home(self, code: str | None = ...) -> None: ...
    def alarm_arm_away(self, code: str | None = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
