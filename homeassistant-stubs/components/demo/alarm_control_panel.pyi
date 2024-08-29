from homeassistant.components.manual.alarm_control_panel import ManualAlarm as ManualAlarm
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ARMING_TIME as CONF_ARMING_TIME, CONF_DELAY_TIME as CONF_DELAY_TIME, CONF_TRIGGER_TIME as CONF_TRIGGER_TIME, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMED_VACATION as STATE_ALARM_ARMED_VACATION, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
