from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from elgato import Elgato as Elgato, Info as Info
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity

class ElgatoEntity(Entity):
    _attr_has_entity_name: bool
    client: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: Elgato, info: Info, mac: Union[str, None]) -> None: ...
