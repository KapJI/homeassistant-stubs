import datetime
from .coordinator import AvmWrapper as AvmWrapper, FRITZ_DATA_KEY as FRITZ_DATA_KEY, FritzConfigEntry as FritzConfigEntry, FritzData as FritzData, FritzDevice as FritzDevice, device_filter_out_from_trackers as device_filter_out_from_trackers
from .entity import FritzDeviceBase as FritzDeviceBase
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: FritzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_add_entities(avm_wrapper: AvmWrapper, async_add_entities: AddConfigEntryEntitiesCallback, data_fritz: FritzData) -> None: ...

class FritzBoxTracker(FritzDeviceBase, ScannerEntity):
    _last_activity: datetime.datetime | None
    def __init__(self, avm_wrapper: AvmWrapper, device: FritzDevice) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
