from .const import DOMAIN as DOMAIN
from .error import PipelineNotFound as PipelineNotFound
from .pipeline import PipelineData as PipelineData, PipelineError as PipelineError, PipelineEvent as PipelineEvent, PipelineEventType as PipelineEventType, PipelineInput as PipelineInput, PipelineRun as PipelineRun, PipelineStage as PipelineStage, async_get_pipeline as async_get_pipeline
from .vad import VoiceCommandSegmenter as VoiceCommandSegmenter
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import conversation as conversation, stt as stt, tts as tts, websocket_api as websocket_api
from homeassistant.const import MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

DEFAULT_TIMEOUT: int
_LOGGER: Incomplete

def async_register_websocket_api(hass: HomeAssistant) -> None: ...
async def websocket_run(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_list_runs(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
def websocket_get_run(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_list_languages(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
