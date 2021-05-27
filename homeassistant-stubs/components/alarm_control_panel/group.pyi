from homeassistant.components.group import GroupIntegrationRegistry as GroupIntegrationRegistry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED, STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_describe_on_off_states(hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...
