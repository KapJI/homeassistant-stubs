from .const import MeshRoles as MeshRoles
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from typing import NotRequired, TypedDict

@dataclass
class Device:
    connected: bool
    connected_to: str
    connection_type: str
    ip_address: str
    name: str
    ssid: str | None
    wan_access: bool | None = ...

class Interface(TypedDict):
    device: str
    mac: str
    op_mode: str
    ssid: str | None
    type: str

HostAttributes = TypedDict('HostAttributes', {'Index': int, 'IPAddress': str, 'MACAddress': str, 'Active': bool, 'HostName': str, 'InterfaceType': str, 'X_AVM-DE_Port': int, 'X_AVM-DE_Speed': int, 'X_AVM-DE_UpdateAvailable': bool, 'X_AVM-DE_UpdateSuccessful': str, 'X_AVM-DE_InfoURL': str | None, 'X_AVM-DE_MACAddressList': str | None, 'X_AVM-DE_Model': str | None, 'X_AVM-DE_URL': str | None, 'X_AVM-DE_Guest': bool, 'X_AVM-DE_RequestClient': str, 'X_AVM-DE_VPN': bool, 'X_AVM-DE_WANAccess': NotRequired[str], 'X_AVM-DE_Disallow': bool, 'X_AVM-DE_IsMeshable': str, 'X_AVM-DE_Priority': str, 'X_AVM-DE_FriendlyName': str, 'X_AVM-DE_FriendlyNameIsWriteable': str})

class HostInfo(TypedDict):
    mac: str
    name: str
    ip: str
    status: bool

class FritzDevice:
    _connected: bool
    _connected_to: str
    _connection_type: str
    _ip_address: str
    _last_activity: datetime | None
    _mac: str
    _name: str
    _ssid: str | None
    _wan_access: bool | None
    def __init__(self, mac: str, dev_info: Device, consider_home: float) -> None: ...
    def update(self, dev_info: Device, consider_home: float) -> None: ...
    @property
    def connected_to(self) -> str: ...
    @property
    def connection_type(self) -> str: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str: ...
    @property
    def ip_address(self) -> str: ...
    @property
    def last_activity(self) -> datetime | None: ...
    @property
    def ssid(self) -> str | None: ...
    @property
    def wan_access(self) -> bool | None: ...
    @wan_access.setter
    def wan_access(self, allowed: bool) -> None: ...

class SwitchInfo(TypedDict):
    description: str
    friendly_name: str
    icon: str
    type: str
    callback_update: Callable
    callback_switch: Callable
    init_state: bool

@dataclass
class ConnectionInfo:
    connection: str
    mesh_role: MeshRoles
    wan_enabled: bool
    ipv6_active: bool
