from .common import FritzBoxTools as FritzBoxTools, FritzData as FritzData, FritzDevice as FritzDevice, FritzDeviceBase as FritzDeviceBase
from .const import DATA_FRITZ as DATA_FRITZ, DOMAIN as DOMAIN
from homeassistant.components.device_tracker import SOURCE_TYPE_ROUTER as SOURCE_TYPE_ROUTER
from homeassistant.components.device_tracker.config_entry import ScannerEntity as ScannerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
YAML_DEFAULT_HOST: str
YAML_DEFAULT_USERNAME: str
PLATFORM_SCHEMA: Any

async def async_get_scanner(hass: HomeAssistant, config: ConfigType) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_add_entities(router: FritzBoxTools, async_add_entities: AddEntitiesCallback, data_fritz: FritzData) -> None: ...

class FritzBoxTracker(FritzDeviceBase, ScannerEntity):
    _last_activity: Any
    _active: bool
    def __init__(self, router: FritzBoxTools, device: FritzDevice) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def source_type(self) -> str: ...
    async def async_process_update(self) -> None: ...
