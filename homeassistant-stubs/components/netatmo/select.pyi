from .const import DATA_HANDLER as DATA_HANDLER, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, EVENT_TYPE_SCHEDULE as EVENT_TYPE_SCHEDULE, MANUFACTURER as MANUFACTURER, SIGNAL_NAME as SIGNAL_NAME, TYPE_ENERGY as TYPE_ENERGY
from .data_handler import CLIMATE_STATE_CLASS_NAME as CLIMATE_STATE_CLASS_NAME, CLIMATE_TOPOLOGY_CLASS_NAME as CLIMATE_TOPOLOGY_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoScheduleSelect(NetatmoBase, SelectEntity):
    _home_id: Any
    _climate_state_class: Any
    _climate_state: Any
    _home: Any
    _device_name: Any
    _attr_name: Any
    _model: str
    _netatmo_type: Any
    _attr_unique_id: Any
    _attr_current_option: Any
    _attr_options: Any
    def __init__(self, data_handler: NetatmoDataHandler, home_id: str, options: list) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def handle_event(self, event: dict) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    def async_update_callback(self) -> None: ...
