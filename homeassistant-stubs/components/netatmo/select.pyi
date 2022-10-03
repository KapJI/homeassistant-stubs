from .const import CONF_URL_ENERGY as CONF_URL_ENERGY, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, EVENT_TYPE_SCHEDULE as EVENT_TYPE_SCHEDULE, NETATMO_CREATE_SELECT as NETATMO_CREATE_SELECT
from .data_handler import HOME as HOME, NetatmoHome as NetatmoHome, SIGNAL_NAME as SIGNAL_NAME
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoScheduleSelect(NetatmoBase, SelectEntity):
    _home: Incomplete
    _home_id: Incomplete
    _signal_name: Incomplete
    _device_name: Incomplete
    _attr_name: Incomplete
    _model: str
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    _attr_options: Incomplete
    def __init__(self, netatmo_home: NetatmoHome) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def handle_event(self, event: dict) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    def async_update_callback(self) -> None: ...
