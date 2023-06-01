from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from tplink_omada_client.devices import OmadaGateway, OmadaSwitch as OmadaSwitch, OmadaSwitchPortDetails
from tplink_omada_client.omadasiteclient import OmadaSiteClient as OmadaSiteClient

POLL_SWITCH_PORT: int
POLL_GATEWAY: int

class OmadaSwitchPortCoordinator(OmadaCoordinator[OmadaSwitchPortDetails]):
    _network_switch: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient, network_switch: OmadaSwitch) -> None: ...
    async def poll_update(self) -> dict[str, OmadaSwitchPortDetails]: ...

class OmadaGatewayCoordinator(OmadaCoordinator[OmadaGateway]):
    mac: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient, mac: str) -> None: ...
    async def poll_update(self) -> dict[str, OmadaGateway]: ...

class OmadaSiteController:
    _gateway_coordinator: OmadaGatewayCoordinator | None
    _initialized_gateway_coordinator: bool
    _hass: Incomplete
    _omada_client: Incomplete
    _switch_port_coordinators: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient) -> None: ...
    @property
    def omada_client(self) -> OmadaSiteClient: ...
    def get_switch_port_coordinator(self, switch: OmadaSwitch) -> OmadaSwitchPortCoordinator: ...
    async def get_gateway_coordinator(self) -> OmadaGatewayCoordinator | None: ...
