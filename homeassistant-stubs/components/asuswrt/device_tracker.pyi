from .const import DATA_ASUSWRT as DATA_ASUSWRT, DOMAIN as DOMAIN
from .router import AsusWrtDevInfo as AsusWrtDevInfo, AsusWrtRouter as AsusWrtRouter
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity, SourceType as SourceType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ATTR_LAST_TIME_REACHABLE: str
DEFAULT_DEVICE_NAME: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def add_entities(router: AsusWrtRouter, async_add_entities: AddEntitiesCallback, tracked: set[str]) -> None: ...

class AsusWrtDevice(ScannerEntity):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    _router: Incomplete
    _device: Incomplete
    _attr_name: Incomplete
    def __init__(self, router: AsusWrtRouter, device: AsusWrtDevInfo) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    def hostname(self) -> str | None: ...
    @property
    def icon(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def mac_address(self) -> str: ...
    _attr_extra_state_attributes: Incomplete
    def async_on_demand_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
