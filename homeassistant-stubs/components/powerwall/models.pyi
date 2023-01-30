from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from requests import Session
from tesla_powerwall import DeviceType as DeviceType, GridStatus as GridStatus, MetersAggregates as MetersAggregates, Powerwall, PowerwallStatus as PowerwallStatus, SiteInfo as SiteInfo, SiteMaster as SiteMaster
from typing import TypedDict

class PowerwallBaseInfo:
    gateway_din: Union[None, str]
    site_info: SiteInfo
    status: PowerwallStatus
    device_type: DeviceType
    serial_numbers: list[str]
    url: str
    def __init__(self, gateway_din, site_info, status, device_type, serial_numbers, url) -> None: ...

class PowerwallData:
    charge: float
    site_master: SiteMaster
    meters: MetersAggregates
    grid_services_active: bool
    grid_status: GridStatus
    backup_reserve: Union[float, None]
    def __init__(self, charge, site_master, meters, grid_services_active, grid_status, backup_reserve) -> None: ...

class PowerwallRuntimeData(TypedDict):
    coordinator: Union[DataUpdateCoordinator[PowerwallData], None]
    api_instance: Powerwall
    base_info: PowerwallBaseInfo
    api_changed: bool
    http_session: Session
