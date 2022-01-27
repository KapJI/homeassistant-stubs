import homeassistant.components.alarm_control_panel as alarm
from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from abodepy.devices.alarm import AbodeAlarm as AbodeAl
from homeassistant.components.alarm_control_panel.const import SUPPORT_ALARM_ARM_AWAY as SUPPORT_ALARM_ARM_AWAY, SUPPORT_ALARM_ARM_HOME as SUPPORT_ALARM_ARM_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ICON: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeAlarm(AbodeDevice, alarm.AlarmControlPanelEntity):
    _attr_icon: Any
    _attr_code_arm_required: bool
    _attr_supported_features: Any
    _device: AbodeAl
    @property
    def state(self) -> Union[str, None]: ...
    def alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
