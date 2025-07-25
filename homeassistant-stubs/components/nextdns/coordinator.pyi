from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nextdns import AnalyticsDnssec, AnalyticsEncryption, AnalyticsIpVersions, AnalyticsProtocols, AnalyticsStatus, ConnectionStatus, NextDns as NextDns, Settings
from nextdns.model import NextDnsData as NextDnsData

_LOGGER: Incomplete

class NextDnsUpdateCoordinator[CoordinatorDataT: NextDnsData](DataUpdateCoordinator[CoordinatorDataT]):
    config_entry: NextDnsConfigEntry
    nextdns: Incomplete
    profile_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NextDnsConfigEntry, nextdns: NextDns, profile_id: str, update_interval: timedelta) -> None: ...
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
