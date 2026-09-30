import probatio
from .const import SIGNAL_KNX_TELEGRAM as SIGNAL_KNX_TELEGRAM
from .schema import ga_validator as ga_validator
from .telegrams import TelegramDict as TelegramDict, decode_telegram_payload as decode_telegram_payload
from .validation import dpt_base_type_validator as dpt_base_type_validator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS, CONF_TYPE as CONF_TYPE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.automation import move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.trigger import Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final, override
from xknx.telegram import Telegram as Telegram
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

TRIGGER_TELEGRAM: Final[str]
CONF_KNX_DESTINATION: Final[str]
CONF_KNX_GROUP_VALUE_WRITE: Final[str]
CONF_KNX_GROUP_VALUE_READ: Final[str]
CONF_KNX_GROUP_VALUE_RESPONSE: Final[str]
CONF_KNX_INCOMING: Final[str]
CONF_KNX_OUTGOING: Final[str]
TELEGRAM_TRIGGER_SCHEMA: dict[probatio.Marker, Any]
_OPTIONS_SCHEMA_DICT: dict[probatio.Marker, Any]
_TELEGRAM_TRIGGER_SCHEMA: Incomplete

@callback
def async_subscribe_telegrams(hass: HomeAssistant, options: ConfigType, telegram_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...

class TelegramTrigger(Trigger):
    _options: dict[str, Any]
    @override
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
