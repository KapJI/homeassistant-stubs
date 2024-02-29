from aionotion.listener.models import ListenerKind as ListenerKind
from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class NotionEntityDescription:
    listener_kind: ListenerKind
    def __init__(self, *, listener_kind) -> None: ...
