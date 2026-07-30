from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_BUTTON as NETATMO_CREATE_BUTTON
from .coordinator import HOME as HOME, NetatmoConfigEntry as NetatmoConfigEntry, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoReachabilityEntity as NetatmoReachabilityEntity
from .helper import device_type_to_str as device_type_to_str
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyatmo import modules as NaModules
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: NetatmoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NetatmoCoverPreferredPositionButton(NetatmoReachabilityEntity, ButtonEntity):
    _attr_configuration_url = CONF_URL_CONTROL
    _attr_entity_registry_enabled_default: bool
    _attr_translation_key: str
    device: NaModules.Shutter
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    @callback
    @override
    def async_update_callback(self) -> None: ...
    @override
    async def async_press(self) -> None: ...
