import asyncio
from .coordinator import TeslemetryEnergyHistoryCoordinator as TeslemetryEnergyHistoryCoordinator, TeslemetryEnergySiteInfoCoordinator as TeslemetryEnergySiteInfoCoordinator, TeslemetryEnergySiteLiveCoordinator as TeslemetryEnergySiteLiveCoordinator, TeslemetryMetadataCoordinator as TeslemetryMetadataCoordinator, TeslemetryVehicleDataCoordinator as TeslemetryVehicleDataCoordinator
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from tesla_fleet_api.const import Scope as Scope
from tesla_fleet_api.teslemetry import EnergySite as EnergySite, Vehicle as Vehicle
from teslemetry_stream import TeslemetryStream as TeslemetryStream, TeslemetryStreamVehicle as TeslemetryStreamVehicle

@dataclass
class TeslemetryData:
    vehicles: list[TeslemetryVehicleData]
    energysites: list[TeslemetryEnergyData]
    scopes: list[Scope]
    stream: TeslemetryStream | None
    metadata_coordinator: TeslemetryMetadataCoordinator

@dataclass
class TeslemetryVehicleData:
    api: Vehicle
    config_entry: ConfigEntry
    coordinator: TeslemetryVehicleDataCoordinator
    poll: bool
    stream: TeslemetryStream
    stream_vehicle: TeslemetryStreamVehicle
    vin: str
    firmware: str
    device: DeviceInfo
    wakelock: asyncio.Lock = field(default_factory=asyncio.Lock)

@dataclass
class TeslemetryEnergyData:
    api: EnergySite
    live_coordinator: TeslemetryEnergySiteLiveCoordinator | None
    info_coordinator: TeslemetryEnergySiteInfoCoordinator
    history_coordinator: TeslemetryEnergyHistoryCoordinator | None
    id: int
    device: DeviceInfo
