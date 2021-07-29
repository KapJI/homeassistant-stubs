from .const import DOMAIN as DOMAIN
from .subscriber import Subscriber as Subscriber
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

_LOGGER: Any

class DevoloDeviceEntity(Entity):
    _device_instance: Any
    _homecontrol: Any
    _attr_available: Any
    _attr_name: Any
    _attr_should_poll: bool
    _attr_unique_id: Any
    _attr_device_info: Any
    subscriber: Any
    sync_callback: Any
    _value: Any
    _unit: str
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _sync(self, message: tuple) -> None: ...
    def _generic_message(self, message: tuple) -> None: ...
