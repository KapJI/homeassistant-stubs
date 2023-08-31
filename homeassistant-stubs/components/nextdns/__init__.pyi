from .const import ATTR_CONNECTION as ATTR_CONNECTION, ATTR_DNSSEC as ATTR_DNSSEC, ATTR_ENCRYPTION as ATTR_ENCRYPTION, ATTR_IP_VERSIONS as ATTR_IP_VERSIONS, ATTR_PROTOCOLS as ATTR_PROTOCOLS, ATTR_SETTINGS as ATTR_SETTINGS, ATTR_STATUS as ATTR_STATUS, CONF_PROFILE_ID as CONF_PROFILE_ID, DOMAIN as DOMAIN, UPDATE_INTERVAL_ANALYTICS as UPDATE_INTERVAL_ANALYTICS, UPDATE_INTERVAL_CONNECTION as UPDATE_INTERVAL_CONNECTION, UPDATE_INTERVAL_SETTINGS as UPDATE_INTERVAL_SETTINGS
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nextdns import AnalyticsDnssec, AnalyticsEncryption, AnalyticsIpVersions, AnalyticsProtocols, AnalyticsStatus, ConnectionStatus, NextDns, Settings
from nextdns.model import NextDnsData
from typing import TypeVar

CoordinatorDataT = TypeVar('CoordinatorDataT', bound=NextDnsData)

class NextDnsUpdateCoordinator(DataUpdateCoordinator[CoordinatorDataT]):
    nextdns: Incomplete
    profile_id: Incomplete
    profile_name: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, nextdns: NextDns, profile_id: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> CoordinatorDataT: ...
    async def _async_update_data_internal(self) -> CoordinatorDataT: ...

class NextDnsStatusUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsStatus]):
    async def _async_update_data_internal(self) -> AnalyticsStatus: ...

class NextDnsDnssecUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsDnssec]):
    async def _async_update_data_internal(self) -> AnalyticsDnssec: ...

class NextDnsEncryptionUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsEncryption]):
    async def _async_update_data_internal(self) -> AnalyticsEncryption: ...

class NextDnsIpVersionsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsIpVersions]):
    async def _async_update_data_internal(self) -> AnalyticsIpVersions: ...

class NextDnsProtocolsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsProtocols]):
    async def _async_update_data_internal(self) -> AnalyticsProtocols: ...

class NextDnsSettingsUpdateCoordinator(NextDnsUpdateCoordinator[Settings]):
    async def _async_update_data_internal(self) -> Settings: ...

class NextDnsConnectionUpdateCoordinator(NextDnsUpdateCoordinator[ConnectionStatus]):
    async def _async_update_data_internal(self) -> ConnectionStatus: ...

_LOGGER: Incomplete
PLATFORMS: Incomplete
COORDINATORS: list[tuple[str, type[NextDnsUpdateCoordinator], timedelta]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
