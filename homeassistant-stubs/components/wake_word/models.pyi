from dataclasses import dataclass

@dataclass(frozen=True)
class WakeWord:
    id: str
    name: str
    phrase: str | None = ...
    def __init__(self, id, name, phrase) -> None: ...

@dataclass
class DetectionResult:
    wake_word_id: str
    wake_word_phrase: str
    timestamp: int | None
    queued_audio: list[tuple[bytes, int]] | None = ...
    def __init__(self, wake_word_id, wake_word_phrase, timestamp, queued_audio) -> None: ...
