from . import OmadaConfigEntry as OmadaConfigEntry
from .coordinator import OmadaClientsCoordinator as OmadaClientsCoordinator, OmadaDevicesCoordinator as OmadaDevicesCoordinator, OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSwitchPortCoordinator as OmadaSwitchPortCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice, OmadaSwitch as OmadaSwitch

class OmadaSiteController:
    _gateway_coordinator: OmadaGatewayCoordinator | None
    _hass: Incomplete
    _config_entry: Incomplete
    _omada_client: Incomplete
    _switch_port_coordinators: dict[str, OmadaSwitchPortCoordinator]
    _devices_coordinator: Incomplete
    _clients_coordinator: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient) -> None: ...
    async def initialize_first_refresh(self) -> None: ...
    async def async_register_device_entities(self, device_filter: Callable[[OmadaListDevice], bool], entity_callback: Callable[[OmadaListDevice], Awaitable[None]]) -> None: ...
    @property
    def omada_client(self) -> OmadaSiteClient: ...
    def get_switch_port_coordinator(self, switch: OmadaSwitch) -> OmadaSwitchPortCoordinator: ...
    @property
    def gateway_coordinator(self) -> OmadaGatewayCoordinator | None: ...
    @property
    def devices_coordinator(self) -> OmadaDevicesCoordinator: ...
    @property
    def clients_coordinator(self) -> OmadaClientsCoordinator: ...
