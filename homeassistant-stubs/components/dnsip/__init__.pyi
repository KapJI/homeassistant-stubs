import aiodns
from .const import CONF_HOSTNAME as CONF_HOSTNAME, CONF_IPV4 as CONF_IPV4, CONF_IPV6 as CONF_IPV6, CONF_PORT_IPV6 as CONF_PORT_IPV6, CONF_RESOLVER as CONF_RESOLVER, CONF_RESOLVER_IPV6 as CONF_RESOLVER_IPV6, DEFAULT_PORT as DEFAULT_PORT, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete

@dataclass
class DnsIPRuntimeData:
    resolver_ipv4: aiodns.DNSResolver | None
    resolver_ipv6: aiodns.DNSResolver | None
type DnsIPConfigEntry = ConfigEntry[DnsIPRuntimeData]

async def async_setup_entry(hass: HomeAssistant, entry: DnsIPConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DnsIPConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: DnsIPConfigEntry) -> bool: ...
