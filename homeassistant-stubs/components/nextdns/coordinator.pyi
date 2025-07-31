from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL_ANALYTICS as UPDATE_INTERVAL_ANALYTICS, UPDATE_INTERVAL_CONNECTION as UPDATE_INTERVAL_CONNECTION, UPDATE_INTERVAL_SETTINGS as UPDATE_INTERVAL_SETTINGS
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
    _update_interval: timedelta
    nextdns: Incomplete
    profile_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NextDnsConfigEntry, nextdns: NextDns, profile_id: str) -> None: ...
    async def _async_update_data(self) -> CoordinatorDataT: ...
    async def _async_update_data_internal(self) -> CoordinatorDataT: ...

class NextDnsStatusUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsStatus]):
    _update_interval = UPDATE_INTERVAL_ANALYTICS
    async def _async_update_data_internal(self) -> AnalyticsStatus: ...

class NextDnsDnssecUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsDnssec]):
    _update_interval = UPDATE_INTERVAL_ANALYTICS
    async def _async_update_data_internal(self) -> AnalyticsDnssec: ...

class NextDnsEncryptionUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsEncryption]):
    _update_interval = UPDATE_INTERVAL_ANALYTICS
    async def _async_update_data_internal(self) -> AnalyticsEncryption: ...

class NextDnsIpVersionsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsIpVersions]):
    _update_interval = UPDATE_INTERVAL_ANALYTICS
    async def _async_update_data_internal(self) -> AnalyticsIpVersions: ...

class NextDnsProtocolsUpdateCoordinator(NextDnsUpdateCoordinator[AnalyticsProtocols]):
    _update_interval = UPDATE_INTERVAL_ANALYTICS
    async def _async_update_data_internal(self) -> AnalyticsProtocols: ...

class NextDnsSettingsUpdateCoordinator(NextDnsUpdateCoordinator[Settings]):
    _update_interval = UPDATE_INTERVAL_SETTINGS
    async def _async_update_data_internal(self) -> Settings: ...

class NextDnsConnectionUpdateCoordinator(NextDnsUpdateCoordinator[ConnectionStatus]):
    _update_interval = UPDATE_INTERVAL_CONNECTION
    async def _async_update_data_internal(self) -> ConnectionStatus: ...
