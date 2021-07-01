from homeassistant.components.automation import AutomationActionType as AutomationActionType
from homeassistant.const import CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import template as template
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONF_EVENT_TYPE: str
CONF_EVENT_CONTEXT: str
TRIGGER_SCHEMA: Any

def _schema_value(value: Any) -> Any: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: dict[str, Any], *, platform_type: str = ...) -> CALLBACK_TYPE: ...
