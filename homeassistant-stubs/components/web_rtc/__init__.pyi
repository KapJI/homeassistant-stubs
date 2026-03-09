from collections.abc import Callable, Iterable
from homeassistant.core import HomeAssistant, callback
from webrtc_models import RTCIceServer

__all__ = ['async_get_ice_servers', 'async_register_ice_servers']

@callback
def async_register_ice_servers(hass: HomeAssistant, get_ice_server_fn: Callable[[], Iterable[RTCIceServer]]) -> Callable[[], None]: ...
@callback
def async_get_ice_servers(hass: HomeAssistant) -> list[RTCIceServer]: ...
