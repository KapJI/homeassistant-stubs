from . import SleepAsAndroidConfigEntry as SleepAsAndroidConfigEntry
from .const import ATTR_EVENT as ATTR_EVENT, MAP_EVENTS as MAP_EVENTS
from .entity import SleepAsAndroidEntity as SleepAsAndroidEntity
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class SleepAsAndroidEventEntityDescription(EventEntityDescription):
    event_types: list[str]

class SleepAsAndroidEvent(StrEnum):
    ALARM_CLOCK = 'alarm_clock'
    USER_NOTIFICATION = 'user_notification'
    SMART_WAKEUP = 'smart_wakeup'
    SLEEP_HEALTH = 'sleep_health'
    LULLABY = 'lullaby'
    SLEEP_PHASE = 'sleep_phase'
    SLEEP_TRACKING = 'sleep_tracking'
    SOUND_EVENT = 'sound_event'
    JET_LAG_PREVENTION = 'jet_lag_prevention'

EVENT_DESCRIPTIONS: tuple[SleepAsAndroidEventEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: SleepAsAndroidConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SleepAsAndroidEventEntity(SleepAsAndroidEntity, EventEntity):
    entity_description: SleepAsAndroidEventEntityDescription
    @callback
    def _async_handle_event(self, webhook_id: str, data: dict[str, str]) -> None: ...
