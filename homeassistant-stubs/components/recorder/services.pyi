from .const import ATTR_APPLY_FILTER as ATTR_APPLY_FILTER, ATTR_KEEP_DAYS as ATTR_KEEP_DAYS, ATTR_REPACK as ATTR_REPACK, DOMAIN as DOMAIN
from .statistics import statistics_during_period as statistics_during_period
from .tasks import PurgeEntitiesTask as PurgeEntitiesTask, PurgeTask as PurgeTask
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers.entityfilter import generate_filter as generate_filter
from homeassistant.helpers.recorder import DATA_INSTANCE as DATA_INSTANCE
from homeassistant.helpers.service import async_extract_entity_ids as async_extract_entity_ids, async_register_admin_service as async_register_admin_service
from homeassistant.util.json import JsonArrayType as JsonArrayType, JsonObjectType as JsonObjectType

SERVICE_PURGE: str
SERVICE_PURGE_ENTITIES: str
SERVICE_ENABLE: str
SERVICE_DISABLE: str
SERVICE_GET_STATISTICS: str
SERVICE_PURGE_SCHEMA: Incomplete
ATTR_DOMAINS: str
ATTR_ENTITY_GLOBS: str
SERVICE_PURGE_ENTITIES_SCHEMA: Incomplete
SERVICE_ENABLE_SCHEMA: Incomplete
SERVICE_DISABLE_SCHEMA: Incomplete
SERVICE_GET_STATISTICS_SCHEMA: Incomplete

async def _async_handle_purge_service(service: ServiceCall) -> None: ...
async def _async_handle_purge_entities_service(service: ServiceCall) -> None: ...
async def _async_handle_enable_service(service: ServiceCall) -> None: ...
async def _async_handle_disable_service(service: ServiceCall) -> None: ...
async def _async_handle_get_statistics_service(service: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
