import webrtcvad
from _typeshed import Incomplete
from collections.abc import Iterable
from enum import StrEnum
from typing import Final

_SAMPLE_RATE: Final[int]
_SAMPLE_WIDTH: Final[int]

class VadSensitivity(StrEnum):
    DEFAULT: str
    RELAXED: str
    AGGRESSIVE: str
    @staticmethod
    def to_seconds(sensitivity: VadSensitivity | str) -> float: ...

class AudioBuffer:
    _buffer: Incomplete
    _length: int
    def __init__(self, maxlen: int) -> None: ...
    @property
    def length(self) -> int: ...
    def clear(self) -> None: ...
    def append(self, data: bytes) -> None: ...
    def bytes(self) -> bytes: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...

class VoiceCommandSegmenter:
    vad_mode: int
    vad_samples_per_chunk: int
    speech_seconds: float
    silence_seconds: float
    timeout_seconds: float
    reset_seconds: float
    in_command: bool
    _speech_seconds_left: float
    _silence_seconds_left: float
    _timeout_seconds_left: float
    _reset_seconds_left: float
    _vad: webrtcvad.Vad
    _leftover_chunk_buffer: AudioBuffer
    _bytes_per_chunk: int
    _seconds_per_chunk: float
    def __post_init__(self) -> None: ...
    def reset(self) -> None: ...
    def process(self, samples: bytes) -> bool: ...
    @property
    def audio_buffer(self) -> bytes: ...
    def _process_chunk(self, chunk: bytes) -> bool: ...
    def __init__(self, vad_mode, vad_samples_per_chunk, speech_seconds, silence_seconds, timeout_seconds, reset_seconds, in_command, _speech_seconds_left, _silence_seconds_left, _timeout_seconds_left, _reset_seconds_left, _vad) -> None: ...

class VoiceActivityTimeout:
    silence_seconds: float
    reset_seconds: float
    vad_mode: int
    vad_samples_per_chunk: int
    _silence_seconds_left: float
    _reset_seconds_left: float
    _vad: webrtcvad.Vad
    _leftover_chunk_buffer: AudioBuffer
    _bytes_per_chunk: int
    _seconds_per_chunk: float
    def __post_init__(self) -> None: ...
    def reset(self) -> None: ...
    def process(self, samples: bytes) -> bool: ...
    def _process_chunk(self, chunk: bytes) -> bool: ...
    def __init__(self, silence_seconds, reset_seconds, vad_mode, vad_samples_per_chunk, _silence_seconds_left, _reset_seconds_left, _vad) -> None: ...

def chunk_samples(samples: bytes, bytes_per_chunk: int, leftover_chunk_buffer: AudioBuffer) -> Iterable[bytes]: ...
