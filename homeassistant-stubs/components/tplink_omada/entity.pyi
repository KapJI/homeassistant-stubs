from .const import DOMAIN as DOMAIN
from .coordinator import OmadaControllerStatusCoordinator as OmadaControllerStatusCoordinator, OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tplink_omada_client import OmadaControllerStatus as OmadaControllerStatus
from tplink_omada_client.devices import OmadaDevice as OmadaDevice, OmadaSwitchPortDetails as OmadaSwitchPortDetails
from typing import Any, override

class OmadaDeviceEntity[_T: OmadaCoordinator[Any]](CoordinatorEntity[_T]):
    _attr_has_entity_name: bool
    device: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _T, device: OmadaDevice) -> None: ...

def get_switch_port_base_name(port: OmadaSwitchPortDetails) -> str: ...

class OmadaControllerEntity(CoordinatorEntity[OmadaControllerStatusCoordinator]):
    _attr_has_entity_name: bool
    _controller_identifier: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OmadaControllerStatusCoordinator) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
