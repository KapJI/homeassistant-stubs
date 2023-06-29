from .const import DOMAIN as DOMAIN
from .error import PipelineNotFound as PipelineNotFound
from .pipeline import Pipeline as Pipeline, PipelineEvent as PipelineEvent, PipelineEventCallback, PipelineEventType as PipelineEventType, async_create_default_pipeline as async_create_default_pipeline, async_get_pipelines as async_get_pipelines
from collections.abc import AsyncIterable
from homeassistant.components import stt
from homeassistant.core import Context, HomeAssistant
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_pipeline_from_audio_stream(hass: HomeAssistant, context: Context, event_callback: PipelineEventCallback, stt_metadata: stt.SpeechMetadata, stt_stream: AsyncIterable[bytes], pipeline_id: str | None = ..., conversation_id: str | None = ..., tts_audio_output: str | None = ..., device_id: str | None = ...) -> None: ...
