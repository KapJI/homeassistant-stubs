from .const import ATTR_END_DATE as ATTR_END_DATE, ATTR_ENTRY_TYPE as ATTR_ENTRY_TYPE, ATTR_INCLUDE_TAGS as ATTR_INCLUDE_TAGS, ATTR_NOTE_TEXT as ATTR_NOTE_TEXT, ATTR_NOTE_TITLE as ATTR_NOTE_TITLE, ATTR_RECIPE_ID as ATTR_RECIPE_ID, ATTR_RESULT_LIMIT as ATTR_RESULT_LIMIT, ATTR_SEARCH_TERMS as ATTR_SEARCH_TERMS, ATTR_START_DATE as ATTR_START_DATE, ATTR_URL as ATTR_URL, DOMAIN as DOMAIN
from .coordinator import MealieConfigEntry as MealieConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_DATE as ATTR_DATE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

SERVICE_GET_MEALPLAN: str
SERVICE_GET_MEALPLAN_SCHEMA: Incomplete
SERVICE_GET_RECIPE: str
SERVICE_GET_RECIPE_SCHEMA: Incomplete
SERVICE_GET_RECIPES: str
SERVICE_GET_RECIPES_SCHEMA: Incomplete
SERVICE_IMPORT_RECIPE: str
SERVICE_IMPORT_RECIPE_SCHEMA: Incomplete
SERVICE_SET_RANDOM_MEALPLAN: str
SERVICE_SET_RANDOM_MEALPLAN_SCHEMA: Incomplete
SERVICE_SET_MEALPLAN: str
SERVICE_SET_MEALPLAN_SCHEMA: Incomplete

def _async_get_entry(call: ServiceCall) -> MealieConfigEntry: ...
async def _async_get_mealplan(call: ServiceCall) -> ServiceResponse: ...
async def _async_get_recipe(call: ServiceCall) -> ServiceResponse: ...
async def _async_get_recipes(call: ServiceCall) -> ServiceResponse: ...
async def _async_import_recipe(call: ServiceCall) -> ServiceResponse: ...
async def _async_set_random_mealplan(call: ServiceCall) -> ServiceResponse: ...
async def _async_set_mealplan(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
