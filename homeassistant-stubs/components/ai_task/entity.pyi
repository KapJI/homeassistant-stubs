import contextlib
from .const import AITaskEntityFeature as AITaskEntityFeature, DEFAULT_SYSTEM_PROMPT as DEFAULT_SYSTEM_PROMPT, DOMAIN as DOMAIN
from .task import GenDataTask as GenDataTask, GenDataTaskResult as GenDataTaskResult, GenImageTask as GenImageTask, GenImageTaskResult as GenImageTaskResult
from _typeshed import Incomplete
from collections.abc import AsyncGenerator
from homeassistant.components.conversation import ChatLog as ChatLog, UserContent as UserContent, async_get_chat_log as async_get_chat_log
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.helpers import llm as llm
from homeassistant.helpers.chat_session import ChatSession as ChatSession
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from propcache.api import cached_property
from typing import final

class AITaskEntity(RestoreEntity):
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    __last_activity: str | None
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def supported_features(self) -> AITaskEntityFeature: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @final
    @contextlib.asynccontextmanager
    async def _async_get_ai_task_chat_log(self, session: ChatSession, task: GenDataTask | GenImageTask) -> AsyncGenerator[ChatLog]: ...
    @final
    async def internal_async_generate_data(self, session: ChatSession, task: GenDataTask) -> GenDataTaskResult: ...
    async def _async_generate_data(self, task: GenDataTask, chat_log: ChatLog) -> GenDataTaskResult: ...
    @final
    async def internal_async_generate_image(self, session: ChatSession, task: GenImageTask) -> GenImageTaskResult: ...
    async def _async_generate_image(self, task: GenImageTask, chat_log: ChatLog) -> GenImageTaskResult: ...
