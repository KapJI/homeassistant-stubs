from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from sfrbox_api.bridge import SFRBox as SFRBox
from sfrbox_api.models import DslInfo as DslInfo, SystemInfo as SystemInfo

class DomainData:
    box: SFRBox
    dsl: SFRDataUpdateCoordinator[DslInfo]
    system: SFRDataUpdateCoordinator[SystemInfo]
    def __init__(self, box, dsl, system) -> None: ...
