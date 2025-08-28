from . import WorkdayConfigEntry as WorkdayConfigEntry
from .const import CONF_EXCLUDES as CONF_EXCLUDES, CONF_OFFSET as CONF_OFFSET, CONF_WORKDAYS as CONF_WORKDAYS
from .entity import BaseWorkdayEntity as BaseWorkdayEntity
from _typeshed import Incomplete
from datetime import datetime
from holidays import HolidayBase as HolidayBase
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from typing import Final

SERVICE_CHECK_DATE: Final[str]
CHECK_DATE: Final[str]

async def async_setup_entry(hass: HomeAssistant, entry: WorkdayConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IsWorkdaySensor(BaseWorkdayEntity, BinarySensorEntity):
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, obj_holidays: HolidayBase, workdays: list[str], excludes: list[str], days_offset: int, name: str, entry_id: str) -> None: ...
    _attr_is_on: Incomplete
    def update_data(self, now: datetime) -> None: ...
