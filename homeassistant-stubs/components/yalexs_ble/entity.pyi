from .const import DOMAIN as DOMAIN
from .models import YaleXSBLEData as YaleXSBLEData
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

class YALEXSBLEEntity(Entity):
    _attr_should_poll: bool
    _data: Incomplete
    _device: Incomplete
    _attr_available: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: YaleXSBLEData) -> None: ...
    def _async_update_state(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
    def _async_state_changed(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
    def _async_device_unavailable(self, _service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
