from . import error as _error, models as _models, run as _run, runtime as _runtime
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import conversation as conversation, stt as stt, tts as tts, websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.collection import CollectionError as CollectionError, ItemNotFound as ItemNotFound, SerializedStorageCollection as SerializedStorageCollection, StorageCollection as StorageCollection, StorageCollectionWebsocket as StorageCollectionWebsocket
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType, VolDictType as VolDictType
from typing import Any, override

PipelineError = _error.PipelineError
PipelineNotFound = _error.PipelineNotFound
PIPELINE_STAGE_ORDER: Incomplete
AudioSettings = _models.AudioSettings
Pipeline = _models.Pipeline
PipelineEvent = _models.PipelineEvent
PipelineEventCallback: Incomplete
PipelineEventType = _models.PipelineEventType
PipelineStage = _models.PipelineStage
WakeWordSettings = _models.WakeWordSettings
STORED_PIPELINE_RUNS: Incomplete
PipelineInput = _run.PipelineInput
PipelineRun = _run.PipelineRun
KEY_ASSIST_PIPELINE: Incomplete
AssistDevice = _runtime.AssistDevice
DeviceAudioQueue = _runtime.DeviceAudioQueue
PipelineData = _runtime.PipelineData
PipelineRunDebug = _runtime.PipelineRunDebug
PipelineRuns = _runtime.PipelineRuns
_LOGGER: Incomplete
STORAGE_KEY: Incomplete
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int
ENGINE_LANGUAGE_PAIRS: Incomplete

def validate_language(data: dict[str, Any]) -> Any: ...

PIPELINE_FIELDS: VolDictType

@callback
def _async_resolve_default_pipeline_settings(hass: HomeAssistant, *, conversation_engine_id: str | None = None, stt_engine_id: str | None = None, tts_engine_id: str | None = None, pipeline_name: str) -> dict[str, str | None]: ...
async def _async_create_default_pipeline(hass: HomeAssistant, pipeline_store: PipelineStorageCollection) -> Pipeline: ...
async def async_create_default_pipeline(hass: HomeAssistant, stt_engine_id: str, tts_engine_id: str, pipeline_name: str) -> Pipeline | None: ...
@callback
def _async_get_pipeline_from_conversation_entity(hass: HomeAssistant, entity_id: str) -> Pipeline: ...
@callback
def async_get_pipeline(hass: HomeAssistant, pipeline_id: str | None = None) -> Pipeline: ...
@callback
def async_get_pipelines(hass: HomeAssistant) -> list[Pipeline]: ...
async def async_update_pipeline(hass: HomeAssistant, pipeline: Pipeline, *, conversation_engine: str | UndefinedType = ..., conversation_language: str | UndefinedType = ..., language: str | UndefinedType = ..., name: str | UndefinedType = ..., stt_engine: str | UndefinedType | None = ..., stt_language: str | UndefinedType | None = ..., tts_engine: str | UndefinedType | None = ..., tts_language: str | UndefinedType | None = ..., tts_voice: str | UndefinedType | None = ..., wake_word_entity: str | UndefinedType | None = ..., wake_word_id: str | UndefinedType | None = ..., prefer_local_intents: bool | UndefinedType = ...) -> None: ...

class PipelinePreferred(CollectionError):
    item_id: Incomplete
    def __init__(self, item_id: str) -> None: ...

class SerializedPipelineStorageCollection(SerializedStorageCollection):
    preferred_item: str

class PipelineStorageCollection(StorageCollection[Pipeline, SerializedPipelineStorageCollection]):
    _preferred_item: str
    @override
    async def _async_load_data(self) -> SerializedPipelineStorageCollection | None: ...
    @override
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    @override
    def _get_suggested_id(self, info: dict) -> str: ...
    @override
    async def _update_data(self, item: Pipeline, update_data: dict) -> Pipeline: ...
    @override
    def _create_item(self, item_id: str, data: dict) -> Pipeline: ...
    @override
    def _deserialize_item(self, data: dict) -> Pipeline: ...
    @override
    def _serialize_item(self, item_id: str, item: Pipeline) -> dict: ...
    @override
    async def async_delete_item(self, item_id: str) -> None: ...
    @callback
    def async_get_preferred_item(self) -> str: ...
    @callback
    def async_set_preferred_item(self, item_id: str) -> None: ...
    @callback
    @override
    def _data_to_save(self) -> SerializedPipelineStorageCollection: ...

class PipelineStorageCollectionWebsocket(StorageCollectionWebsocket[PipelineStorageCollection]):
    @callback
    @override
    def async_setup(self, hass: HomeAssistant) -> None: ...
    @override
    async def ws_delete_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    @callback
    def ws_get_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    @callback
    @override
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
    async def ws_set_preferred_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class PipelineStore(Store[SerializedPipelineStorageCollection]):
    @override
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: SerializedPipelineStorageCollection) -> SerializedPipelineStorageCollection: ...

async def async_setup_pipeline_store(hass: HomeAssistant) -> PipelineData: ...
