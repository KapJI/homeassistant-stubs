from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from dataclasses import dataclass

@dataclass(slots=True)
class TPLinkData:
    parent_coordinator: TPLinkDataUpdateCoordinator
    children_coordinators: list[TPLinkDataUpdateCoordinator]
    def __init__(self, parent_coordinator, children_coordinators) -> None: ...
