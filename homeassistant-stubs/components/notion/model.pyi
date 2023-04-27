from aionotion.sensor.models import ListenerKind as ListenerKind

class NotionEntityDescriptionMixin:
    listener_kind: ListenerKind
    def __init__(self, listener_kind) -> None: ...
