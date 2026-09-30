from aioesphomeapi import OutgoingConnectionServer, ReconnectLogic as ReconnectLogic
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.util.hass_dict import HassKey as HassKey

_KEY_OUTGOING_CONNECTION_SERVER: HassKey[OutgoingConnectionServer]

@callback
def _async_get_server(hass: HomeAssistant) -> OutgoingConnectionServer: ...
@callback
def async_register_outgoing_target(hass: HomeAssistant, mac: str, reconnect_logic: ReconnectLogic) -> CALLBACK_TYPE | None: ...
