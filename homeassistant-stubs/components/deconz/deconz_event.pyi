from .const import CONF_ANGLE as CONF_ANGLE, CONF_GESTURE as CONF_GESTURE, LOGGER as LOGGER
from .deconz_device import DeconzBase as DeconzBase
from .gateway import DeconzGateway as DeconzGateway
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_EVENT as CONF_EVENT, CONF_ID as CONF_ID, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_XY as CONF_XY
from homeassistant.core import callback as callback
from homeassistant.util import slugify as slugify
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.ancillary_control import AncillaryControl
from pydeconz.models.sensor.switch import Switch

CONF_DECONZ_EVENT: str
CONF_DECONZ_ALARM_EVENT: str
SUPPORTED_DECONZ_ALARM_EVENTS: Incomplete

async def async_setup_events(gateway: DeconzGateway) -> None: ...
def async_unload_events(gateway: DeconzGateway) -> None: ...

class DeconzEventBase(DeconzBase):
    _unsubscribe: Incomplete
    device: Incomplete
    device_id: Incomplete
    event_id: Incomplete
    def __init__(self, device: Union[AncillaryControl, Switch], gateway: DeconzGateway) -> None: ...
    def async_will_remove_from_hass(self) -> None: ...
    def async_update_callback(self) -> None: ...
    async def async_update_device_registry(self) -> None: ...

class DeconzEvent(DeconzEventBase):
    _device: Switch
    def async_update_callback(self) -> None: ...

class DeconzAlarmEvent(DeconzEventBase):
    _device: AncillaryControl
    def async_update_callback(self) -> None: ...
