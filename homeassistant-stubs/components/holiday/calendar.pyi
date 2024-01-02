from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from holidays import HolidayBase as HolidayBase
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HolidayCalendarEntity(CalendarEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _country: Incomplete
    _province: Incomplete
    _location: Incomplete
    _language: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _obj_holidays: Incomplete
    def __init__(self, name: str, country: str, province: str | None, language: str, obj_holidays: HolidayBase, unique_id: str) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
