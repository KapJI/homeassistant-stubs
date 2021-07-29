from . import SimpliSafe as SimpliSafe, SimpliSafeEntity as SimpliSafeEntity
from .const import ATTR_ALARM_DURATION as ATTR_ALARM_DURATION, ATTR_ALARM_VOLUME as ATTR_ALARM_VOLUME, ATTR_CHIME_VOLUME as ATTR_CHIME_VOLUME, ATTR_ENTRY_DELAY_AWAY as ATTR_ENTRY_DELAY_AWAY, ATTR_ENTRY_DELAY_HOME as ATTR_ENTRY_DELAY_HOME, ATTR_EXIT_DELAY_AWAY as ATTR_EXIT_DELAY_AWAY, ATTR_EXIT_DELAY_HOME as ATTR_EXIT_DELAY_HOME, ATTR_LIGHT as ATTR_LIGHT, ATTR_VOICE_PROMPT_VOLUME as ATTR_VOICE_PROMPT_VOLUME, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER, VOLUME_STRING_MAP as VOLUME_STRING_MAP
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, FORMAT_NUMBER as FORMAT_NUMBER, FORMAT_TEXT as FORMAT_TEXT
from homeassistant.components.alarm_control_panel.const import SUPPORT_ALARM_ARM_AWAY as SUPPORT_ALARM_ARM_AWAY, SUPPORT_ALARM_ARM_HOME as SUPPORT_ALARM_ARM_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMING as STATE_ALARM_ARMING, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.system.v2 import SystemV2 as SystemV2
from simplipy.system.v3 import SystemV3
from typing import Any

ATTR_BATTERY_BACKUP_POWER_LEVEL: str
ATTR_GSM_STRENGTH: str
ATTR_PIN_NAME: str
ATTR_RF_JAMMING: str
ATTR_WALL_POWER_LEVEL: str
ATTR_WIFI_STRENGTH: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimpliSafeAlarm(SimpliSafeEntity, AlarmControlPanelEntity):
    _attr_code_format: Any
    _attr_supported_features: Any
    _last_event: Any
    _attr_state: Any
    def __init__(self, simplisafe: SimpliSafe, system: Union[SystemV2, SystemV3]) -> None: ...
    def _is_code_valid(self, code: Union[str, None], state: str) -> bool: ...
    async def async_alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    def async_update_from_rest_api(self) -> None: ...
