from .const import DOMAIN as DOMAIN
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

class NanoleafEntity(Entity):
    _nanoleaf: Any
    _attr_device_info: Any
    def __init__(self, nanoleaf: Nanoleaf) -> None: ...
