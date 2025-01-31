from .const import ATTR_ARGS as ATTR_ARGS, ATTR_CONFIG_ENTRY as ATTR_CONFIG_ENTRY, ATTR_DATA as ATTR_DATA, ATTR_DIRECTION as ATTR_DIRECTION, ATTR_ITEM as ATTR_ITEM, ATTR_KEYWORD as ATTR_KEYWORD, ATTR_PATH as ATTR_PATH, ATTR_PRIORITY as ATTR_PRIORITY, ATTR_SKILL as ATTR_SKILL, ATTR_TAG as ATTR_TAG, ATTR_TARGET as ATTR_TARGET, ATTR_TASK as ATTR_TASK, ATTR_TYPE as ATTR_TYPE, DOMAIN as DOMAIN, EVENT_API_CALL_SUCCESS as EVENT_API_CALL_SUCCESS, SERVICE_ABORT_QUEST as SERVICE_ABORT_QUEST, SERVICE_ACCEPT_QUEST as SERVICE_ACCEPT_QUEST, SERVICE_API_CALL as SERVICE_API_CALL, SERVICE_CANCEL_QUEST as SERVICE_CANCEL_QUEST, SERVICE_CAST_SKILL as SERVICE_CAST_SKILL, SERVICE_GET_TASKS as SERVICE_GET_TASKS, SERVICE_LEAVE_QUEST as SERVICE_LEAVE_QUEST, SERVICE_REJECT_QUEST as SERVICE_REJECT_QUEST, SERVICE_SCORE_HABIT as SERVICE_SCORE_HABIT, SERVICE_SCORE_REWARD as SERVICE_SCORE_REWARD, SERVICE_START_QUEST as SERVICE_START_QUEST, SERVICE_TRANSFORMATION as SERVICE_TRANSFORMATION
from .types import HabiticaConfigEntry as HabiticaConfigEntry
from _typeshed import Incomplete
from habiticalib import TaskData as TaskData
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_NAME as ATTR_NAME, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

_LOGGER: Incomplete
SERVICE_API_CALL_SCHEMA: Incomplete
SERVICE_CAST_SKILL_SCHEMA: Incomplete
SERVICE_MANAGE_QUEST_SCHEMA: Incomplete
SERVICE_SCORE_TASK_SCHEMA: Incomplete
SERVICE_TRANSFORMATION_SCHEMA: Incomplete
SERVICE_GET_TASKS_SCHEMA: Incomplete
SKILL_MAP: Incomplete
COST_MAP: Incomplete
ITEMID_MAP: Incomplete

def get_config_entry(hass: HomeAssistant, entry_id: str) -> HabiticaConfigEntry: ...
def async_setup_services(hass: HomeAssistant) -> None: ...
