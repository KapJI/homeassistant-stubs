from .common import AvmWrapper as AvmWrapper, FritzData as FritzData, FritzDevice as FritzDevice, FritzDeviceBase as FritzDeviceBase, device_filter_out_from_trackers as device_filter_out_from_trackers
from .const import DATA_FRITZ as DATA_FRITZ, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType
from homeassistant.components.device_tracker.config_entry import ScannerEntity as ScannerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
YAML_DEFAULT_HOST: str
YAML_DEFAULT_USERNAME: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_add_entities(avm_wrapper: AvmWrapper, async_add_entities: AddEntitiesCallback, data_fritz: FritzData) -> None: ...

class FritzBoxTracker(FritzDeviceBase, ScannerEntity):
    _last_activity: Incomplete
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
    @property
    def source_type(self) -> SourceType: ...
