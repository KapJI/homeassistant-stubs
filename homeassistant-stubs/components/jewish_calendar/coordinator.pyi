import datetime as dt
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from hdate import HDateInfo, Location as Location, Zmanim
from hdate.translator import Language as Language
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type JewishCalendarConfigEntry = ConfigEntry[JewishCalendarUpdateCoordinator]

@dataclass
class JewishCalendarData:
    language: Language
    diaspora: bool
    location: Location
    candle_lighting_offset: int
    havdalah_offset: int
    dateinfo: HDateInfo | None = ...
    zmanim: Zmanim | None = ...

class JewishCalendarUpdateCoordinator(DataUpdateCoordinator[JewishCalendarData]):
    config_entry: JewishCalendarConfigEntry
    event_unsub: CALLBACK_TYPE | None
    data: Incomplete
    _unsub_update: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, data: JewishCalendarData) -> None: ...
    async def _async_update_data(self) -> JewishCalendarData: ...
    @callback
    def async_schedule_future_update(self) -> None: ...
    @callback
    def _handle_midnight_update(self, _now: dt.datetime) -> None: ...
    async def async_shutdown(self) -> None: ...
    def make_zmanim(self, date: dt.date) -> Zmanim: ...
    @property
    def zmanim(self) -> Zmanim: ...
    @property
    def dateinfo(self) -> HDateInfo: ...
