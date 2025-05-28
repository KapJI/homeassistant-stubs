import datetime as dt
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from hdate import HDateInfo as HDateInfo, Location as Location, Zmanim
from hdate.translator import Language as Language
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

type JewishCalendarConfigEntry = ConfigEntry[JewishCalendarData]
@dataclass
class JewishCalendarDataResults:
    daytime_date: HDateInfo
    after_shkia_date: HDateInfo
    after_tzais_date: HDateInfo
    zmanim: Zmanim

@dataclass
class JewishCalendarData:
    language: Language
    diaspora: bool
    location: Location
    candle_lighting_offset: int
    havdalah_offset: int
    results: JewishCalendarDataResults | None = ...

class JewishCalendarEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    data: Incomplete
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: EntityDescription) -> None: ...
    def make_zmanim(self, date: dt.date) -> Zmanim: ...
