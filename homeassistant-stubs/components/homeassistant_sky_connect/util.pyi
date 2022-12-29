from homeassistant.components import usb as usb
from homeassistant.config_entries import ConfigEntry as ConfigEntry

def get_usb_service_info(config_entry: ConfigEntry) -> usb.UsbServiceInfo: ...
