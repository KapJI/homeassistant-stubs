from dataclasses import dataclass
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo

@dataclass(slots=True)
class ESPHomeServiceInfo(BaseServiceInfo):
    name: str
    zwave_home_id: int | None
    ip_address: str
    port: int
    noise_psk: str | None = ...
    @property
    def socket_path(self) -> str: ...
