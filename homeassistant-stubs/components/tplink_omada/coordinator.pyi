from . import OmadaConfigEntry as OmadaConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient, OmadaSwitchPortDetails
from tplink_omada_client.clients import OmadaWirelessClient
from tplink_omada_client.devices import OmadaGateway, OmadaListDevice, OmadaSwitch as OmadaSwitch

_LOGGER: Incomplete
POLL_SWITCH_PORT: int
POLL_GATEWAY: int
POLL_CLIENTS: int
POLL_DEVICES: int

class OmadaCoordinator[_T](DataUpdateCoordinator[dict[str, _T]]):
    config_entry: OmadaConfigEntry
    omada_client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient, name: str, poll_delay: int | None = 300) -> None: ...
    async def _async_update_data(self) -> dict[str, _T]: ...
    async def poll_update(self) -> dict[str, _T]: ...

class OmadaSwitchPortCoordinator(OmadaCoordinator[OmadaSwitchPortDetails]):
    _network_switch: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient, network_switch: OmadaSwitch) -> None: ...
    async def poll_update(self) -> dict[str, OmadaSwitchPortDetails]: ...

class OmadaGatewayCoordinator(OmadaCoordinator[OmadaGateway]):
    mac: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient, mac: str) -> None: ...
    async def poll_update(self) -> dict[str, OmadaGateway]: ...

class OmadaDevicesCoordinator(OmadaCoordinator[OmadaListDevice]):
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient) -> None: ...
    async def poll_update(self) -> dict[str, OmadaListDevice]: ...

class OmadaClientsCoordinator(OmadaCoordinator[OmadaWirelessClient]):
    def __init__(self, hass: HomeAssistant, config_entry: OmadaConfigEntry, omada_client: OmadaSiteClient) -> None: ...
    async def poll_update(self) -> dict[str, OmadaWirelessClient]: ...
