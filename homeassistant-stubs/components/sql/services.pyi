from .const import CONF_QUERY as CONF_QUERY, DOMAIN as DOMAIN
from .util import async_create_sessionmaker as async_create_sessionmaker, check_and_render_sql_query as check_and_render_sql_query, convert_value as convert_value, generate_lambda_stmt as generate_lambda_stmt, redact_credentials as redact_credentials, resolve_db_url as resolve_db_url, validate_query as validate_query, validate_sql_select as validate_sql_select
from _typeshed import Incomplete
from homeassistant.components.recorder import CONF_DB_URL as CONF_DB_URL, get_instance as get_instance
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.trigger_template_entity import ValueTemplate as ValueTemplate
from homeassistant.util.json import JsonValueType as JsonValueType
from sqlalchemy.engine import Result as Result
from sqlalchemy.orm import Session as Session

_LOGGER: Incomplete
SERVICE_QUERY: str
SERVICE_QUERY_SCHEMA: Incomplete

async def _async_query_service(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
