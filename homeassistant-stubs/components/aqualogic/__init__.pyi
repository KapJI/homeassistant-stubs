import threading
from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from aqualogic.core import AquaLogic
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override

_LOGGER: Incomplete
RECONNECT_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete
type AquaLogicConfigEntry = ConfigEntry[AquaLogicProcessor]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_import(hass: HomeAssistant, conf: dict) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AquaLogicConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AquaLogicConfigEntry) -> bool: ...

class AquaLogicProcessor(threading.Thread):
    _hass: Incomplete
    _host: Incomplete
    _port: Incomplete
    _shutdown: bool
    _panel: AquaLogic | None
    def __init__(self, hass: HomeAssistant, host: str, port: int) -> None: ...
    def shutdown(self) -> None: ...
    def data_changed(self, panel: AquaLogic) -> None: ...
    @override
    def run(self) -> None: ...
    @property
    def panel(self) -> AquaLogic | None: ...
