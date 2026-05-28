from _typeshed import Incomplete
from enum import StrEnum
from typing import Self

DOMAIN: str
ATTR_AFTER_SUNSET: str
ATTR_NUSACH: str
CONF_ALTITUDE: str
CONF_DIASPORA: str
CONF_CANDLE_LIGHT_MINUTES: str
CONF_HAVDALAH_OFFSET_MINUTES: str
CONF_DAILY_EVENTS: str
CONF_YEARLY_EVENTS: str
CONF_LEARNING_SCHEDULE: str
DEFAULT_NAME: str
DEFAULT_CANDLE_LIGHT: int
DEFAULT_DIASPORA: bool
DEFAULT_HAVDALAH_OFFSET_MINUTES: int
DEFAULT_LANGUAGE: str

class DailyCalendarEventType(StrEnum):
    DATE = 'date'
    ALOT_HASHACHAR = ('alot_hashachar', 'Alot Hashachar', 'Halachic dawn')
    NETZ_HACHAMA = ('netz_hachama', 'Netz Hachama', 'Halachic sunrise')
    SOF_ZMAN_SHEMA_GRA = ('sof_zman_shema_gra', 'Sof Zman Shema (Gr"A)', 'Latest time for Shema')
    SOF_ZMAN_SHEMA_MGA = ('sof_zman_shema_mga', 'Sof Zman Shema (Mg"A)', 'Latest time for Shema')
    SOF_ZMAN_TFILLA_GRA = ('sof_zman_tfilla_gra', 'Sof Zman Tefilla (Gr"A)', 'Latest time for Tefilla')
    SOF_ZMAN_TFILLA_MGA = ('sof_zman_tfilla_mga', 'Sof Zman Tefilla (Mg"A)', 'Latest time for Tefilla')
    CHATZOT_HAYOM = ('chatzot_hayom', 'Chatzot Hayom', 'Halachic midday')
    MINCHA_GEDOLA = ('mincha_gedola', 'Mincha Gedola', 'Earliest time for Mincha')
    MINCHA_KETANA = ('mincha_ketana', 'Mincha Ketana', 'Preferable time for Mincha')
    PLAG_HAMINCHA = ('plag_hamincha', 'Plag Hamincha', 'Plag Hamincha')
    SHKIA = ('shkia', 'Shkia', 'Sunset')
    TSET_HAKOHAVIM = ('tset_hakohavim_tsom', "T'set Hakochavim", 'Nightfall')
    _summary: str
    _description_prefix: str
    def __new__(cls, value: str, summary: str = '', description_prefix: str = '') -> Self: ...
    @property
    def summary(self) -> str: ...
    @property
    def description_prefix(self) -> str: ...

class YearlyCalendarEventType(StrEnum):
    HOLIDAY = 'holiday'
    WEEKLY_PORTION = 'weekly_portion'
    OMER_COUNT = 'omer_count'
    CANDLE_LIGHTING = 'candle_lighting'
    HAVDALAH = 'havdalah'

class LearningScheduleEventType(StrEnum):
    DAF_YOMI = 'daf_yomi'

DEFAULT_CALENDAR_EVENTS: Incomplete
SERVICE_COUNT_OMER: str
