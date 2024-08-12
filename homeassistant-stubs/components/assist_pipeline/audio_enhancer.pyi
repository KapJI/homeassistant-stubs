import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass

_LOGGER: Incomplete

@dataclass(frozen=True, slots=True)
class EnhancedAudioChunk:
    audio: bytes
    timestamp_ms: int
    is_speech: bool | None
    def __init__(self, audio, timestamp_ms, is_speech) -> None: ...

class AudioEnhancer(ABC, metaclass=abc.ABCMeta):
    auto_gain: Incomplete
    noise_suppression: Incomplete
    is_vad_enabled: Incomplete
    def __init__(self, auto_gain: int, noise_suppression: int, is_vad_enabled: bool) -> None: ...
    @abstractmethod
    def enhance_chunk(self, audio: bytes, timestamp_ms: int) -> EnhancedAudioChunk: ...
    @property
    @abstractmethod
    def samples_per_chunk(self) -> int | None: ...

class MicroVadEnhancer(AudioEnhancer):
    vad: Incomplete
    threshold: float
    def __init__(self, auto_gain: int, noise_suppression: int, is_vad_enabled: bool) -> None: ...
    def enhance_chunk(self, audio: bytes, timestamp_ms: int) -> EnhancedAudioChunk: ...
    @property
    def samples_per_chunk(self) -> int | None: ...
