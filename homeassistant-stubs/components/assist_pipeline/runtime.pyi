import asyncio
from .const import DOMAIN as DOMAIN
from .models import PipelineEvent as PipelineEvent
from .pipeline import PipelineStorageCollection as PipelineStorageCollection
from .run import PipelineRun as PipelineRun
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.helpers.collection import CHANGE_UPDATED as CHANGE_UPDATED
from homeassistant.util import ulid as ulid_util
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.limited_size_dict import LimitedSizeDict as LimitedSizeDict

class PipelineRuns:
    _pipeline_runs: dict[str, dict[str, PipelineRun]]
    _pipeline_store: Incomplete
    def __init__(self, pipeline_store: PipelineStorageCollection) -> None: ...
    def add_run(self, pipeline_run: PipelineRun) -> None: ...
    def remove_run(self, pipeline_run: PipelineRun) -> None: ...
    async def _change_listener(self, change_type: str, item_id: str, change: dict) -> None: ...

@dataclass(slots=True)
class DeviceAudioQueue:
    queue: asyncio.Queue[bytes | None]
    id: str = field(default_factory=ulid_util.ulid_now)
    overflow: bool = ...

@dataclass(slots=True)
class AssistDevice:
    domain: str
    unique_id_prefix: str

class PipelineData:
    pipeline_store: Incomplete
    pipeline_debug: dict[str, LimitedSizeDict[str, PipelineRunDebug]]
    pipeline_devices: dict[str, AssistDevice]
    pipeline_runs: Incomplete
    device_audio_queues: dict[str, DeviceAudioQueue]
    def __init__(self, pipeline_store: PipelineStorageCollection) -> None: ...

@dataclass(slots=True)
class PipelineRunDebug:
    events: list[PipelineEvent] = field(default_factory=list, init=False)
    timestamp: str = field(default_factory=Incomplete, init=False)

KEY_ASSIST_PIPELINE: HassKey[PipelineData]
