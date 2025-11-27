import asyncio
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete

@dataclass
class ProvisioningState:
    event: asyncio.Event = field(default_factory=asyncio.Event)
    host: str | None = ...
    port: int | None = ...

PROVISIONING_FUTURES: HassKey[dict[str, ProvisioningState]]

@callback
def async_get_provisioning_registry(hass: HomeAssistant) -> dict[str, ProvisioningState]: ...
@callback
def async_register_zeroconf_discovery(hass: HomeAssistant, mac: str, host: str, port: int) -> None: ...
