from .const import DEFAULT_PIPELINE_TIMEOUT as DEFAULT_PIPELINE_TIMEOUT, DEFAULT_WAKE_WORD_TIMEOUT as DEFAULT_WAKE_WORD_TIMEOUT, DOMAIN as DOMAIN, EVENT_RECORDING as EVENT_RECORDING
from .error import PipelineNotFound as PipelineNotFound
from .pipeline import AudioSettings as AudioSettings, DeviceAudioQueue as DeviceAudioQueue, PipelineData as PipelineData, PipelineError as PipelineError, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineInput as PipelineInput, PipelineRun as PipelineRun, PipelineStage as PipelineStage, WakeWordSettings as WakeWordSettings, async_get_pipeline as async_get_pipeline
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import conversation as conversation, stt as stt, tts as tts, websocket_api as websocket_api
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_SECONDS as ATTR_SECONDS, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Final

_LOGGER: Incomplete
CAPTURE_RATE: Final[int]
CAPTURE_WIDTH: Final[int]
CAPTURE_CHANNELS: Final[int]
MAX_CAPTURE_TIMEOUT: Final[float]

def async_register_websocket_api(hass: HomeAssistant) -> None: ...
async def websocket_run(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_list_runs(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_get_run(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_list_languages(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_device_capture(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
