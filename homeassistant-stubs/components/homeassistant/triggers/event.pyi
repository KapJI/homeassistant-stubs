from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_PLATFORM as CONF_PLATFORM, EVENT_STATE_REPORTED as EVENT_STATE_REPORTED
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr, template as template
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
CONF_EVENT_TYPE: str
CONF_EVENT_CONTEXT: str

def _validate_event_types(value: Any) -> Any: ...

TRIGGER_SCHEMA: Incomplete

async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
@callback
def _log_composite_device_id_warning(hass: HomeAssistant, config: ConfigType, device_id: str, split_devices: list[dr.DeviceEntry]) -> None: ...
def _schema_value(value: Any) -> Any: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo, *, platform_type: str = 'event') -> CALLBACK_TYPE: ...
