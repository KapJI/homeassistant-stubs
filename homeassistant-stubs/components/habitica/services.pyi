from .const import ATTR_ADD_CHECKLIST_ITEM as ATTR_ADD_CHECKLIST_ITEM, ATTR_ALIAS as ATTR_ALIAS, ATTR_CLEAR_DATE as ATTR_CLEAR_DATE, ATTR_CLEAR_REMINDER as ATTR_CLEAR_REMINDER, ATTR_CONFIG_ENTRY as ATTR_CONFIG_ENTRY, ATTR_COST as ATTR_COST, ATTR_COUNTER_DOWN as ATTR_COUNTER_DOWN, ATTR_COUNTER_UP as ATTR_COUNTER_UP, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_FREQUENCY as ATTR_FREQUENCY, ATTR_INTERVAL as ATTR_INTERVAL, ATTR_ITEM as ATTR_ITEM, ATTR_KEYWORD as ATTR_KEYWORD, ATTR_NOTES as ATTR_NOTES, ATTR_PRIORITY as ATTR_PRIORITY, ATTR_REMINDER as ATTR_REMINDER, ATTR_REMOVE_CHECKLIST_ITEM as ATTR_REMOVE_CHECKLIST_ITEM, ATTR_REMOVE_REMINDER as ATTR_REMOVE_REMINDER, ATTR_REMOVE_TAG as ATTR_REMOVE_TAG, ATTR_REPEAT as ATTR_REPEAT, ATTR_REPEAT_MONTHLY as ATTR_REPEAT_MONTHLY, ATTR_SCORE_CHECKLIST_ITEM as ATTR_SCORE_CHECKLIST_ITEM, ATTR_SKILL as ATTR_SKILL, ATTR_START_DATE as ATTR_START_DATE, ATTR_STREAK as ATTR_STREAK, ATTR_TAG as ATTR_TAG, ATTR_TARGET as ATTR_TARGET, ATTR_TASK as ATTR_TASK, ATTR_TYPE as ATTR_TYPE, ATTR_UNSCORE_CHECKLIST_ITEM as ATTR_UNSCORE_CHECKLIST_ITEM, ATTR_UP_DOWN as ATTR_UP_DOWN, DOMAIN as DOMAIN, SERVICE_ABORT_QUEST as SERVICE_ABORT_QUEST, SERVICE_ACCEPT_QUEST as SERVICE_ACCEPT_QUEST, SERVICE_CANCEL_QUEST as SERVICE_CANCEL_QUEST, SERVICE_CAST_SKILL as SERVICE_CAST_SKILL, SERVICE_CREATE_DAILY as SERVICE_CREATE_DAILY, SERVICE_CREATE_HABIT as SERVICE_CREATE_HABIT, SERVICE_CREATE_REWARD as SERVICE_CREATE_REWARD, SERVICE_CREATE_TODO as SERVICE_CREATE_TODO, SERVICE_GET_TASKS as SERVICE_GET_TASKS, SERVICE_LEAVE_QUEST as SERVICE_LEAVE_QUEST, SERVICE_REJECT_QUEST as SERVICE_REJECT_QUEST, SERVICE_SCORE_HABIT as SERVICE_SCORE_HABIT, SERVICE_SCORE_REWARD as SERVICE_SCORE_REWARD, SERVICE_START_QUEST as SERVICE_START_QUEST, SERVICE_TRANSFORMATION as SERVICE_TRANSFORMATION, SERVICE_UPDATE_DAILY as SERVICE_UPDATE_DAILY, SERVICE_UPDATE_HABIT as SERVICE_UPDATE_HABIT, SERVICE_UPDATE_REWARD as SERVICE_UPDATE_REWARD, SERVICE_UPDATE_TODO as SERVICE_UPDATE_TODO, WEEK_DAYS as WEEK_DAYS
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry
from _typeshed import Incomplete
from habiticalib import TaskData as TaskData
from homeassistant.components.todo import ATTR_RENAME as ATTR_RENAME
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DATE as ATTR_DATE, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

_LOGGER: Incomplete
SERVICE_CAST_SKILL_SCHEMA: Incomplete
SERVICE_MANAGE_QUEST_SCHEMA: Incomplete
SERVICE_SCORE_TASK_SCHEMA: Incomplete
SERVICE_TRANSFORMATION_SCHEMA: Incomplete
BASE_TASK_SCHEMA: Incomplete
SERVICE_UPDATE_TASK_SCHEMA: Incomplete
SERVICE_CREATE_TASK_SCHEMA: Incomplete
SERVICE_DAILY_SCHEMA: Incomplete
SERVICE_GET_TASKS_SCHEMA: Incomplete
SKILL_MAP: Incomplete
COST_MAP: Incomplete
ITEMID_MAP: Incomplete
SERVICE_TASK_TYPE_MAP: Incomplete

def get_config_entry(hass: HomeAssistant, entry_id: str) -> HabiticaConfigEntry: ...
async def _cast_skill(call: ServiceCall) -> ServiceResponse: ...
async def _manage_quests(call: ServiceCall) -> ServiceResponse: ...
async def _score_task(call: ServiceCall) -> ServiceResponse: ...
async def _transformation(call: ServiceCall) -> ServiceResponse: ...
async def _get_tasks(call: ServiceCall) -> ServiceResponse: ...
async def _create_or_update_task(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
