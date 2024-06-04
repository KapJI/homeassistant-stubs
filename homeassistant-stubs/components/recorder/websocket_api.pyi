from .models import StatisticPeriod as StatisticPeriod
from .statistics import STATISTIC_UNIT_TO_UNIT_CONVERTER as STATISTIC_UNIT_TO_UNIT_CONVERTER, async_add_external_statistics as async_add_external_statistics, async_change_statistics_unit as async_change_statistics_unit, async_import_statistics as async_import_statistics, async_list_statistic_ids as async_list_statistic_ids, list_statistic_ids as list_statistic_ids, statistic_during_period as statistic_during_period, statistics_during_period as statistics_during_period, validate_statistics as validate_statistics
from .util import PERIOD_SCHEMA as PERIOD_SCHEMA, get_instance as get_instance, resolve_period as resolve_period
from _typeshed import Incomplete
from datetime import datetime as dt
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.websocket_api import messages as messages
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.json import json_bytes as json_bytes
from homeassistant.util.unit_conversion import DataRateConverter as DataRateConverter, DistanceConverter as DistanceConverter, DurationConverter as DurationConverter, ElectricCurrentConverter as ElectricCurrentConverter, ElectricPotentialConverter as ElectricPotentialConverter, EnergyConverter as EnergyConverter, InformationConverter as InformationConverter, MassConverter as MassConverter, PowerConverter as PowerConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, UnitlessRatioConverter as UnitlessRatioConverter, VolumeConverter as VolumeConverter, VolumeFlowRateConverter as VolumeFlowRateConverter
from typing import Any, Literal

UNIT_SCHEMA: Incomplete

def async_setup(hass: HomeAssistant) -> None: ...
def _ws_get_statistic_during_period(hass: HomeAssistant, msg_id: int, start_time: dt | None, end_time: dt | None, statistic_id: str, types: set[Literal['max', 'mean', 'min', 'change']] | None, units: dict[str, str]) -> bytes: ...
async def ws_get_statistic_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _ws_get_statistics_during_period(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: dt | None, statistic_ids: set[str] | None, period: Literal['5minute', 'day', 'hour', 'week', 'month'], units: dict[str, str], types: set[Literal['change', 'last_reset', 'max', 'mean', 'min', 'state', 'sum']]) -> bytes: ...
async def ws_handle_get_statistics_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_get_statistics_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _ws_get_list_statistic_ids(hass: HomeAssistant, msg_id: int, statistic_type: Literal['mean', 'sum'] | None = None) -> bytes: ...
async def ws_handle_list_statistic_ids(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...
async def ws_list_statistic_ids(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def ws_validate_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def ws_clear_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def ws_get_statistics_metadata(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def ws_update_statistics_metadata(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def ws_change_statistics_unit(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def ws_adjust_sum_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def ws_import_statistics(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def ws_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
