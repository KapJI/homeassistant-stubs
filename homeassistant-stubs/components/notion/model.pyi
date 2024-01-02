from aionotion.sensor.models import ListenerKind as ListenerKind
from dataclasses import dataclass

@dataclass(frozen=True)
class NotionEntityDescriptionMixin:
    listener_kind: ListenerKind
    def __init__(self, listener_kind) -> None: ...
