from .const import HardwareVariant as HardwareVariant
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo

_LOGGER: Incomplete

def get_usb_service_info(config_entry: ConfigEntry) -> UsbServiceInfo: ...
def get_hardware_variant(config_entry: ConfigEntry) -> HardwareVariant: ...
