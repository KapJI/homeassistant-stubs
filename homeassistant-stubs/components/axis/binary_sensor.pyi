from .device import AxisNetworkDevice as AxisNetworkDevice
from .entity import AxisEventEntity as AxisEventEntity
from _typeshed import Incomplete
from axis.models.event import Event as Event
from axis.vapix.interfaces.applications.fence_guard import FenceGuardHandler as FenceGuardHandler
from axis.vapix.interfaces.applications.loitering_guard import LoiteringGuardHandler as LoiteringGuardHandler
from axis.vapix.interfaces.applications.motion_guard import MotionGuardHandler as MotionGuardHandler
from axis.vapix.interfaces.applications.vmd4 import Vmd4Handler as Vmd4Handler
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later

DEVICE_CLASS: Incomplete
EVENT_TOPICS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisBinarySensor(AxisEventEntity, BinarySensorEntity):
    cancel_scheduled_update: Incomplete
    _attr_device_class: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, event: Event, device: AxisNetworkDevice) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...
    _attr_name: Incomplete
    def _set_name(self, event: Event) -> None: ...
