from .const import DOMAIN as DOMAIN
from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client.devices import OmadaSwitch as OmadaSwitch, OmadaSwitchPortDetails

class OmadaSwitchDeviceEntity(CoordinatorEntity[OmadaCoordinator[OmadaSwitchPortDetails]]):
    device: Incomplete
    def __init__(self, coordinator: OmadaCoordinator[OmadaSwitchPortDetails], device: OmadaSwitch) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
