from .const import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, DATA_COMPONENT as DATA_COMPONENT
from _typeshed import Incomplete
from homeassistant.const import ATTR_CODE as ATTR_CODE, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_CUSTOM_BYPASS as SERVICE_ALARM_ARM_CUSTOM_BYPASS, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_ARM_VACATION as SERVICE_ALARM_ARM_VACATION, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_ALARM_TRIGGER as SERVICE_ALARM_TRIGGER
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.config_validation import make_entity_service_schema as make_entity_service_schema
from typing import Final

ALARM_SERVICE_SCHEMA: Final[Incomplete]

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
