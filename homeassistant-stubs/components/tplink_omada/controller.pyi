from .coordinator import OmadaClientsCoordinator as OmadaClientsCoordinator, OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSwitchPortCoordinator as OmadaSwitchPortCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient
from tplink_omada_client.devices import OmadaSwitch as OmadaSwitch

class OmadaSiteController:
    _gateway_coordinator: OmadaGatewayCoordinator | None
    _initialized_gateway_coordinator: bool
    _clients_coordinator: OmadaClientsCoordinator | None
    _hass: Incomplete
    _omada_client: Incomplete
    _switch_port_coordinators: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient) -> None: ...
    @property
    def omada_client(self) -> OmadaSiteClient: ...
    def get_switch_port_coordinator(self, switch: OmadaSwitch) -> OmadaSwitchPortCoordinator: ...
    async def get_gateway_coordinator(self) -> OmadaGatewayCoordinator | None: ...
    def get_clients_coordinator(self) -> OmadaClientsCoordinator: ...
