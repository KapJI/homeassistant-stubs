from . import DriverEvents as DriverEvents
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.const import LogLevel as LogLevel

@dataclass
class ZwaveJSData:
    client: ZwaveClient
    driver_events: DriverEvents
    old_server_log_level: LogLevel | None = ...
type ZwaveJSConfigEntry = ConfigEntry[ZwaveJSData]
