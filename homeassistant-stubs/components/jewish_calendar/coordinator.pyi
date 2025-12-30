import datetime as dt
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from hdate import HDateInfo, Location as Location, Zmanim
from hdate.translator import Language as Language
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type JewishCalendarConfigEntry = ConfigEntry[JewishCalendarUpdateCoordinator]

@dataclass(frozen=True)
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
    _attr_should_poll: bool
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, data: JewishCalendarData) -> None: ...
    _unsub_refresh: Incomplete
    async def _async_update_data(self) -> JewishCalendarData: ...
    @callback
    def _handle_midnight_update(self, _now: dt.datetime) -> None: ...
    def make_zmanim(self, date: dt.date) -> Zmanim: ...
    @property
    def zmanim(self) -> Zmanim: ...
    @property
    def dateinfo(self) -> HDateInfo: ...
