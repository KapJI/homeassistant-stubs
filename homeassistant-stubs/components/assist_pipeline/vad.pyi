import webrtcvad
from homeassistant.backports.enum import StrEnum as StrEnum

_SAMPLE_RATE: int

class VadSensitivity(StrEnum):
    DEFAULT: str
    RELAXED: str
    AGGRESSIVE: str
    @staticmethod
    def to_seconds(sensitivity: VadSensitivity | str) -> float: ...

class VoiceCommandSegmenter:
    vad_mode: int
    vad_frames: int
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
    _audio_buffer: bytes
    _bytes_per_chunk: int
    _seconds_per_chunk: float
    def __post_init__(self) -> None: ...
    def reset(self) -> None: ...
    def process(self, samples: bytes) -> bool: ...
    def _process_chunk(self, chunk: bytes) -> bool: ...
    def __init__(self, vad_mode, vad_frames, speech_seconds, silence_seconds, timeout_seconds, reset_seconds, in_command, _speech_seconds_left, _silence_seconds_left, _timeout_seconds_left, _reset_seconds_left, _vad, _audio_buffer, _bytes_per_chunk, _seconds_per_chunk) -> None: ...
