from homeassistant.components import network as network
from homeassistant.core import HomeAssistant as HomeAssistant
from ipaddress import IPv4Address, IPv6Address

async def async_build_source_set(hass: HomeAssistant) -> set[IPv4Address | IPv6Address]: ...
