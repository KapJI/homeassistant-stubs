from dataclasses import dataclass
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Final

ATTR_PROPERTIES_ID: Final[str]

@dataclass(slots=True)
class ZeroconfServiceInfo(BaseServiceInfo):
    ip_address: IPv4Address | IPv6Address
    ip_addresses: list[IPv4Address | IPv6Address]
    port: int | None
    hostname: str
    type: str
    name: str
    properties: dict[str, Any]
    @property
    def host(self) -> str: ...
    @property
    def addresses(self) -> list[str]: ...
