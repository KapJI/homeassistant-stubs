import io
import voluptuous as vol
from .const import AITaskEntityFeature as AITaskEntityFeature, DATA_COMPONENT as DATA_COMPONENT, DATA_MEDIA_SOURCE as DATA_MEDIA_SOURCE, DATA_PREFERENCES as DATA_PREFERENCES, DOMAIN as DOMAIN, IMAGE_DIR as IMAGE_DIR, IMAGE_EXPIRY_TIME as IMAGE_EXPIRY_TIME
from dataclasses import dataclass
from homeassistant.components import camera as camera, conversation as conversation, image as image, media_source as media_source
from homeassistant.components.http.auth import async_sign_path as async_sign_path
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import llm as llm
from homeassistant.helpers.chat_session import ChatSession as ChatSession, async_get_chat_session as async_get_chat_session
from homeassistant.util import RE_SANITIZE_FILENAME as RE_SANITIZE_FILENAME, slugify as slugify
from pathlib import Path
from typing import Any

def _save_camera_snapshot(image_data: camera.Image | image.Image) -> Path: ...
async def _resolve_attachments(hass: HomeAssistant, session: ChatSession, attachments: list[dict] | None = None) -> list[conversation.Attachment]: ...
async def async_generate_data(hass: HomeAssistant, *, task_name: str, entity_id: str | None = None, instructions: str, structure: vol.Schema | None = None, attachments: list[dict] | None = None, llm_api: llm.API | None = None) -> GenDataTaskResult: ...
async def async_generate_image(hass: HomeAssistant, *, task_name: str, entity_id: str | None = None, instructions: str, attachments: list[dict] | None = None) -> ServiceResponse: ...

@dataclass(slots=True)
class GenDataTask:
    name: str
    instructions: str
    structure: vol.Schema | None = ...
    attachments: list[conversation.Attachment] | None = ...
    llm_api: llm.API | None = ...
    def __str__(self) -> str: ...

@dataclass(slots=True)
class GenDataTaskResult:
    conversation_id: str
    data: Any
    def as_dict(self) -> dict[str, Any]: ...

@dataclass(slots=True)
class GenImageTask:
    name: str
    instructions: str
    attachments: list[conversation.Attachment] | None = ...
    def __str__(self) -> str: ...

@dataclass(slots=True)
class GenImageTaskResult:
    image_data: bytes
    conversation_id: str
    mime_type: str
    width: int | None = ...
    height: int | None = ...
    model: str | None = ...
    revised_prompt: str | None = ...
    def as_dict(self) -> dict[str, Any]: ...

@dataclass(slots=True)
class ImageData:
    filename: str
    file: io.IOBase
    content_type: str
