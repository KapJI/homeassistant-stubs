from collections.abc import Mapping
from dataclasses import dataclass, field
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from typing import Any, Final

ATTR_ST: Final[str]
ATTR_NT: Final[str]
ATTR_UPNP_DEVICE_TYPE: Final[str]
ATTR_UPNP_FRIENDLY_NAME: Final[str]
ATTR_UPNP_MANUFACTURER: Final[str]
ATTR_UPNP_MANUFACTURER_URL: Final[str]
ATTR_UPNP_MODEL_DESCRIPTION: Final[str]
ATTR_UPNP_MODEL_NAME: Final[str]
ATTR_UPNP_MODEL_NUMBER: Final[str]
ATTR_UPNP_MODEL_URL: Final[str]
ATTR_UPNP_SERIAL: Final[str]
ATTR_UPNP_SERVICE_LIST: Final[str]
ATTR_UPNP_UDN: Final[str]
ATTR_UPNP_UPC: Final[str]
ATTR_UPNP_PRESENTATION_URL: Final[str]

@dataclass(slots=True)
class SsdpServiceInfo(BaseServiceInfo):
    ssdp_usn: str
    ssdp_st: str
    upnp: Mapping[str, Any]
    ssdp_location: str | None = ...
    ssdp_nt: str | None = ...
    ssdp_udn: str | None = ...
    ssdp_ext: str | None = ...
    ssdp_server: str | None = ...
    ssdp_headers: Mapping[str, Any] = field(default_factory=dict)
    ssdp_all_locations: set[str] = field(default_factory=set)
    x_homeassistant_matching_domains: set[str] = field(default_factory=set)
