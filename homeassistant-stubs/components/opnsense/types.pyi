from aiopnsense import OPNsenseClient as OPNsenseClient
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from typing import Any

@dataclass(slots=True)
class OPNsenseRuntimeData:
    client: OPNsenseClient
    tracker_interfaces: list[str]
type DeviceDetails = dict[str, Any]
type DeviceDetailsByMAC = dict[str, DeviceDetails]
type OPNsenseConfigEntry = ConfigEntry[OPNsenseRuntimeData]
