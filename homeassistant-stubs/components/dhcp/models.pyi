import dataclasses
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.loader import DHCPMatcher as DHCPMatcher
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import TypedDict

@dataclass(slots=True)
class DhcpMatchers:
    registered_devices_domains: set[str]
    no_oui_matchers: dict[str, list[DHCPMatcher]]
    oui_matchers: dict[str, list[DHCPMatcher]]

class DHCPAddressData(TypedDict):
    hostname: str
    ip: str

@dataclasses.dataclass(slots=True)
class DHCPData:
    integration_matchers: DhcpMatchers
    callbacks: set[Callable[[dict[str, DHCPAddressData]], None]] = dataclasses.field(default_factory=set)
    address_data: dict[str, DHCPAddressData] = dataclasses.field(default_factory=dict)

DATA_DHCP: HassKey[DHCPData]
