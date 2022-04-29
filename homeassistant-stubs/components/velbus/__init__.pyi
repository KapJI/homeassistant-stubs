from .const import CONF_INTERFACE as CONF_INTERFACE, CONF_MEMO_TEXT as CONF_MEMO_TEXT, DOMAIN as DOMAIN, SERVICE_SCAN as SERVICE_SCAN, SERVICE_SET_MEMO_TEXT as SERVICE_SET_MEMO_TEXT, SERVICE_SYNC as SERVICE_SYNC
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from velbusaio.channels import Channel as VelbusChannel
from velbusaio.controller import Velbus

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def velbus_connect_task(controller: Velbus, hass: HomeAssistant, entry_id: str) -> None: ...
def _migrate_device_identifiers(hass: HomeAssistant, entry_id: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class VelbusEntity(Entity):
    _attr_should_poll: bool
    _channel: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, channel: VelbusChannel) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _on_update(self) -> None: ...
