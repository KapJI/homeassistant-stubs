from .const import DOMAIN as DOMAIN
from .triggers import turn_on as turn_on
from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo, TriggerProtocol as TriggerProtocol
from homeassistant.helpers.typing import ConfigType as ConfigType

TRIGGERS: Incomplete

def _get_trigger_platform(config: ConfigType) -> TriggerProtocol: ...
async def async_validate_trigger_config(hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
