import logging
from .const import MAX_QUEUE_BACKLOG as MAX_QUEUE_BACKLOG
from .statistics import STATISTIC_UNIT_TO_UNIT_CONVERTER as STATISTIC_UNIT_TO_UNIT_CONVERTER, async_add_external_statistics as async_add_external_statistics, async_change_statistics_unit as async_change_statistics_unit, async_import_statistics as async_import_statistics, list_statistic_ids as list_statistic_ids, statistics_during_period as statistics_during_period, validate_statistics as validate_statistics
from .util import async_migration_in_progress as async_migration_in_progress, async_migration_is_live as async_migration_is_live, get_instance as get_instance
from datetime import datetime as dt
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import messages as messages
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter, EnergyConverter as EnergyConverter, MassConverter as MassConverter, PowerConverter as PowerConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, VolumeConverter as VolumeConverter
from typing import Literal

_LOGGER: logging.Logger

def async_setup(hass: HomeAssistant) -> None: ...
def _ws_get_statistics_during_period(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: Union[dt, None], statistic_ids: Union[list[str], None], period: Literal['5minute', 'day', 'hour', 'month'], units: dict[str, str]) -> str: ...
async def ws_handle_get_statistics_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_get_statistics_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def _ws_get_list_statistic_ids(hass: HomeAssistant, msg_id: int, statistic_type: Union[Literal['mean'], Literal['sum'], None] = ...) -> str: ...
async def ws_handle_list_statistic_ids(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_list_statistic_ids(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_validate_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def ws_clear_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_get_statistics_metadata(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def ws_update_statistics_metadata(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def ws_change_statistics_unit(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_adjust_sum_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def ws_import_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
def ws_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_backup_start(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_backup_end(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
