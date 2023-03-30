from .coordinator import OmadaCoordinator as OmadaCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from tplink_omada_client.devices import OmadaSwitch as OmadaSwitch, OmadaSwitchPortDetails
from tplink_omada_client.omadasiteclient import OmadaSiteClient as OmadaSiteClient

POLL_SWITCH_PORT: int

class OmadaSwitchPortCoordinator(OmadaCoordinator[OmadaSwitchPortDetails]):
    _network_switch: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient, network_switch: OmadaSwitch) -> None: ...
    async def poll_update(self) -> dict[str, OmadaSwitchPortDetails]: ...

class OmadaSiteController:
    _hass: Incomplete
    _omada_client: Incomplete
    _switch_port_coordinators: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient) -> None: ...
    @property
    def omada_client(self) -> OmadaSiteClient: ...
    def get_switch_port_coordinator(self, switch: OmadaSwitch) -> OmadaSwitchPortCoordinator: ...
