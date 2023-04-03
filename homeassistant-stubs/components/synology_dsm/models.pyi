from .common import SynoApi as SynoApi
from .coordinator import SynologyDSMCameraUpdateCoordinator as SynologyDSMCameraUpdateCoordinator, SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMSwitchUpdateCoordinator as SynologyDSMSwitchUpdateCoordinator

class SynologyDSMData:
    api: SynoApi
    coordinator_central: SynologyDSMCentralUpdateCoordinator
    coordinator_cameras: SynologyDSMCameraUpdateCoordinator | None
    coordinator_switches: SynologyDSMSwitchUpdateCoordinator | None
    def __init__(self, api, coordinator_central, coordinator_cameras, coordinator_switches) -> None: ...
