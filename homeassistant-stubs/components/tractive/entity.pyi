from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

class TractiveEntity(Entity):
    _attr_device_info: Incomplete
    _user_id: Incomplete
    _tracker_id: Incomplete
    _trackable: Incomplete
    def __init__(self, user_id: str, trackable: dict[str, Any], tracker_details: dict[str, Any]) -> None: ...
