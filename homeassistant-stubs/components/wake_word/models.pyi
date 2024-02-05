from dataclasses import dataclass

@dataclass(frozen=True)
class WakeWord:
    id: str
    name: str
    def __init__(self, id, name) -> None: ...

@dataclass
class DetectionResult:
    wake_word_id: str
    timestamp: int | None
    queued_audio: list[tuple[bytes, int]] | None = ...
    def __init__(self, wake_word_id, timestamp, queued_audio) -> None: ...
