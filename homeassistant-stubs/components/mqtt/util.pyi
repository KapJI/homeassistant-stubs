import asyncio
import logging
from .const import ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_QOS as ATTR_QOS, ATTR_RETAIN as ATTR_RETAIN, ATTR_TOPIC as ATTR_TOPIC, CONF_CERTIFICATE as CONF_CERTIFICATE, CONF_CLIENT_CERT as CONF_CLIENT_CERT, CONF_CLIENT_KEY as CONF_CLIENT_KEY, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_QOS as DEFAULT_QOS, DEFAULT_RETAIN as DEFAULT_RETAIN, DOMAIN as DOMAIN
from .models import DATA_MQTT as DATA_MQTT, DATA_MQTT_AVAILABLE as DATA_MQTT_AVAILABLE, ReceiveMessage as ReceiveMessage
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from functools import lru_cache
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, Platform as Platform, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import template as template
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any

AVAILABILITY_TIMEOUT: float
TEMP_DIR_NAME: Incomplete
_VALID_QOS_SCHEMA: Incomplete
_LOGGER: Incomplete

class EnsureJobAfterCooldown:
    _loop: Incomplete
    _timeout: Incomplete
    _callback: Incomplete
    _task: asyncio.Task | None
    _timer: asyncio.TimerHandle | None
    _next_execute_time: float
    def __init__(self, timeout: float, callback_job: Callable[[], Coroutine[Any, None, None]]) -> None: ...
    def set_timeout(self, timeout: float) -> None: ...
    async def _async_job(self) -> None: ...
    @callback
    def _async_task_done(self, task: asyncio.Task) -> None: ...
    @callback
    def async_execute(self) -> asyncio.Task: ...
    @callback
    def _async_cancel_timer(self) -> None: ...
    @callback
    def async_schedule(self) -> None: ...
    @callback
    def _async_timer_reached(self) -> None: ...
    async def async_cleanup(self) -> None: ...

def platforms_from_config(config: list[ConfigType]) -> set[Platform | str]: ...
async def async_forward_entry_setup_and_setup_discovery(hass: HomeAssistant, config_entry: ConfigEntry, platforms: set[Platform | str], late: bool = False) -> None: ...
def mqtt_config_entry_enabled(hass: HomeAssistant) -> bool | None: ...
async def async_wait_for_mqtt_client(hass: HomeAssistant) -> bool: ...
def valid_topic(topic: Any) -> str: ...
@lru_cache
def valid_subscribe_topic(topic: Any) -> str: ...
def valid_subscribe_topic_template(value: Any) -> template.Template: ...
@lru_cache
def valid_publish_topic(topic: Any) -> str: ...
def valid_qos_schema(qos: Any) -> int: ...

_MQTT_WILL_BIRTH_SCHEMA: Incomplete

def valid_birth_will(config: ConfigType) -> ConfigType: ...
async def async_create_certificate_temp_files(hass: HomeAssistant, config: ConfigType) -> None: ...
def check_state_too_long(logger: logging.Logger, proposed_state: str, entity_id: str, msg: ReceiveMessage) -> bool: ...
def get_file_path(option: str, default: str | None = None) -> str | None: ...
def migrate_certificate_file_to_content(file_name_or_auto: str) -> str | None: ...
@callback
def learn_more_url(platform: str) -> str: ...
