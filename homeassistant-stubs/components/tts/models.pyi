from dataclasses import dataclass

@dataclass(frozen=True)
class Voice:
    voice_id: str
    name: str
    def __init__(self, voice_id, name) -> None: ...
