from RFXtrx import RFXtrxDevice as RFXtrxDevice
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_get_device_object(hass: HomeAssistant, device_id: str) -> RFXtrxDevice: ...
