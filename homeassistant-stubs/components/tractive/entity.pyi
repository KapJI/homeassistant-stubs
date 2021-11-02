from .const import DOMAIN as DOMAIN
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

class TractiveEntity(Entity):
    _attr_device_info: Any
    _user_id: Any
    _tracker_id: Any
    _trackable: Any
    def __init__(self, user_id: str, trackable: dict[str, Any], tracker_details: dict[str, Any]) -> None: ...
