from .coordinator import PrivateDevicesCoordinator as PrivateDevicesCoordinator
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
PRIVATE_BLE_DEVICE_DATA: HassKey[PrivateDevicesCoordinator]
