from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from sfrbox_api.bridge import SFRBox as SFRBox
from sfrbox_api.models import DslInfo as DslInfo, FtthInfo as FtthInfo, SystemInfo as SystemInfo, WanInfo as WanInfo

class DomainData:
    box: SFRBox
    dsl: SFRDataUpdateCoordinator[DslInfo]
    ftth: SFRDataUpdateCoordinator[FtthInfo]
    system: SFRDataUpdateCoordinator[SystemInfo]
    wan: SFRDataUpdateCoordinator[WanInfo]
    def __init__(self, box, dsl, ftth, system, wan) -> None: ...
