from typing import TypedDict

class IPv6ConfiguredAddress(TypedDict):
    address: str
    flowinfo: int
    scope_id: int
    network_prefix: int

class IPv4ConfiguredAddress(TypedDict):
    address: str
    network_prefix: int

class Adapter(TypedDict):
    name: str
    index: int | None
    enabled: bool
    auto: bool
    default: bool
    ipv6: list[IPv6ConfiguredAddress]
    ipv4: list[IPv4ConfiguredAddress]
