import datetime
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, setup as setup
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_MEGA_WATT_HOUR as ENERGY_MEGA_WATT_HOUR, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, Platform as Platform, SOUND_PRESSURE_DB as SOUND_PRESSURE_DB, TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
COMPONENTS_WITH_CONFIG_ENTRY_DEMO_PLATFORM: Incomplete
COMPONENTS_WITH_DEMO_PLATFORM: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _generate_mean_statistics(start: datetime.datetime, end: datetime.datetime, init_value: float, max_diff: float) -> list[StatisticData]: ...
async def _insert_sum_statistics(hass: HomeAssistant, metadata: StatisticMetaData, start: datetime.datetime, end: datetime.datetime, max_diff: float) -> None: ...
async def _insert_statistics(hass: HomeAssistant) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def finish_setup(hass: HomeAssistant, config: ConfigType) -> None: ...
