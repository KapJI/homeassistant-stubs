from .const import HOSTNAME as HOSTNAME, IP_ADDRESS as IP_ADDRESS
from .models import DATA_DHCP as DATA_DHCP, DHCPAddressData as DHCPAddressData
from collections.abc import Callable as Callable
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.service_info.dhcp import DhcpServiceInfo as DhcpServiceInfo

@callback
def async_register_dhcp_callback_internal(hass: HomeAssistant, callback_: Callable[[dict[str, DHCPAddressData]], None]) -> CALLBACK_TYPE: ...
@callback
def async_get_address_data_internal(hass: HomeAssistant) -> dict[str, DHCPAddressData]: ...
@callback
def async_discovered_service_info(hass: HomeAssistant) -> list[DhcpServiceInfo]: ...
