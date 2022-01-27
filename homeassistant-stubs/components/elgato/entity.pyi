from .const import DOMAIN as DOMAIN
from elgato import Elgato as Elgato, Info as Info
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

class ElgatoEntity(Entity):
    client: Any
    _attr_device_info: Any
    def __init__(self, client: Elgato, info: Info, mac: Union[str, None]) -> None: ...
