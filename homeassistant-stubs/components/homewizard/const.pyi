from aiohwenergy.device import Device
from homeassistant.const import Platform as Platform
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, TypedDict

DOMAIN: str
PLATFORMS: Any
CONF_API_ENABLED: str
CONF_DATA: str
CONF_DEVICE: str
CONF_PATH: str
CONF_PRODUCT_NAME: str
CONF_PRODUCT_TYPE: str
CONF_SERIAL: str
UPDATE_INTERVAL: Any

class DeviceResponseEntry(TypedDict):
    device: Device
    data: dict[str, StateType]
