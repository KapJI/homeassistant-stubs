from .coordinator import SolarLogBasicDataCoordinator as SolarLogBasicDataCoordinator, SolarLogDeviceDataCoordinator as SolarLogDeviceDataCoordinator, SolarLogLongtimeDataCoordinator as SolarLogLongtimeDataCoordinator
from dataclasses import dataclass
from solarlog_cli.solarlog_connector import SolarLogConnector as SolarLogConnector

@dataclass
class SolarlogIntegrationData:
    api: SolarLogConnector
    basic_data_coordinator: SolarLogBasicDataCoordinator
    device_data_coordinator: SolarLogDeviceDataCoordinator | None = ...
    longtime_data_coordinator: SolarLogLongtimeDataCoordinator | None = ...
