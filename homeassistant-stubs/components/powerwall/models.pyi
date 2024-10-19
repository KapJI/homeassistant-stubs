from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from tesla_powerwall import BatteryResponse as BatteryResponse, DeviceType as DeviceType, GridStatus as GridStatus, MetersAggregatesResponse as MetersAggregatesResponse, Powerwall as Powerwall, PowerwallStatusResponse as PowerwallStatusResponse, SiteInfoResponse as SiteInfoResponse, SiteMasterResponse as SiteMasterResponse
from typing import TypedDict

@dataclass
class PowerwallBaseInfo:
    gateway_din: str
    site_info: SiteInfoResponse
    status: PowerwallStatusResponse
    device_type: DeviceType
    serial_numbers: list[str]
    url: str
    batteries: dict[str, BatteryResponse]
    def __init__(self, gateway_din, site_info, status, device_type, serial_numbers, url, batteries) -> None: ...

@dataclass
class PowerwallData:
    charge: float
    site_master: SiteMasterResponse
    meters: MetersAggregatesResponse
    grid_services_active: bool
    grid_status: GridStatus
    backup_reserve: float | None
    batteries: dict[str, BatteryResponse]
    def __init__(self, charge, site_master, meters, grid_services_active, grid_status, backup_reserve, batteries) -> None: ...

class PowerwallRuntimeData(TypedDict):
    coordinator: DataUpdateCoordinator[PowerwallData] | None
    api_instance: Powerwall
    base_info: PowerwallBaseInfo
    api_changed: bool
