from .models import DATA_DHCP as DATA_DHCP, DHCPAddressData as DHCPAddressData
from collections.abc import Callable as Callable
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback

@callback
def async_register_dhcp_callback_internal(hass: HomeAssistant, callback_: Callable[[dict[str, DHCPAddressData]], None]) -> CALLBACK_TYPE: ...
@callback
def async_get_address_data_internal(hass: HomeAssistant) -> dict[str, DHCPAddressData]: ...
