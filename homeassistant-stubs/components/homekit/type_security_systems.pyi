from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import CHAR_CURRENT_SECURITY_STATE as CHAR_CURRENT_SECURITY_STATE, CHAR_TARGET_SECURITY_STATE as CHAR_TARGET_SECURITY_STATE, SERV_SECURITY_SYSTEM as SERV_SECURITY_SYSTEM
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, DOMAIN as DOMAIN
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMED_VACATION as STATE_ALARM_ARMED_VACATION, STATE_ALARM_ARMING as STATE_ALARM_ARMING, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import State as State, callback as callback
from typing import Any

_LOGGER: Incomplete
HK_ALARM_STAY_ARMED: int
HK_ALARM_AWAY_ARMED: int
HK_ALARM_NIGHT_ARMED: int
HK_ALARM_DISARMED: int
HK_ALARM_TRIGGERED: int
HASS_TO_HOMEKIT_CURRENT: Incomplete
HASS_TO_HOMEKIT_TARGET: Incomplete
HASS_TO_HOMEKIT_SERVICES: Incomplete
HK_TO_SERVICE: Incomplete

class SecuritySystem(HomeAccessory):
    _alarm_code: Incomplete
    char_current_state: Incomplete
    char_target_state: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def set_security_state(self, value: int) -> None: ...
    def async_update_state(self, new_state: State) -> None: ...
