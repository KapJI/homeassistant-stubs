from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_BUTTON as NETATMO_CREATE_BUTTON
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoModuleEntity as NetatmoModuleEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyatmo import modules as NaModules

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NetatmoCoverPreferredPositionButton(NetatmoModuleEntity, ButtonEntity):
    _attr_configuration_url = CONF_URL_CONTROL
    _attr_entity_registry_enabled_default: bool
    _attr_translation_key: str
    device: NaModules.Shutter
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
    async def async_press(self) -> None: ...
