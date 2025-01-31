from dataclasses import dataclass
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo

@dataclass(slots=True)
class DhcpServiceInfo(BaseServiceInfo):
    ip: str
    hostname: str
    macaddress: str
