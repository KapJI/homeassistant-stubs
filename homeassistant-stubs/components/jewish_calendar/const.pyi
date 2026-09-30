from _typeshed import Incomplete
from enum import StrEnum

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
    ALOT_HASHACHAR = 'alot_hashachar'
    NETZ_HACHAMA = 'netz_hachama'
    SOF_ZMAN_SHEMA_GRA = 'sof_zman_shema_gra'
    SOF_ZMAN_SHEMA_MGA = 'sof_zman_shema_mga'
    SOF_ZMAN_TFILLA_GRA = 'sof_zman_tfilla_gra'
    SOF_ZMAN_TFILLA_MGA = 'sof_zman_tfilla_mga'
    CHATZOT_HAYOM = 'chatzot_hayom'
    MINCHA_GEDOLA = 'mincha_gedola'
    MINCHA_KETANA = 'mincha_ketana'
    PLAG_HAMINCHA = 'plag_hamincha'
    SHKIA = 'shkia'
    TSET_HAKOHAVIM = 'tset_hakohavim_tsom'

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
