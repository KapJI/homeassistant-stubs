from .common import NoMatchingShoppingListItem as NoMatchingShoppingListItem, _get_shopping_data as _get_shopping_data
from .const import ATTR_REVERSE as ATTR_REVERSE, DEFAULT_REVERSE as DEFAULT_REVERSE, DOMAIN as DOMAIN, SERVICE_ADD_ITEM as SERVICE_ADD_ITEM, SERVICE_CLEAR_COMPLETED_ITEMS as SERVICE_CLEAR_COMPLETED_ITEMS, SERVICE_COMPLETE_ALL as SERVICE_COMPLETE_ALL, SERVICE_COMPLETE_ITEM as SERVICE_COMPLETE_ITEM, SERVICE_INCOMPLETE_ALL as SERVICE_INCOMPLETE_ALL, SERVICE_INCOMPLETE_ITEM as SERVICE_INCOMPLETE_ITEM, SERVICE_REMOVE_ITEM as SERVICE_REMOVE_ITEM, SERVICE_SORT as SERVICE_SORT
from _typeshed import Incomplete
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback

_LOGGER: Incomplete
SERVICE_ITEM_SCHEMA: Incomplete
SERVICE_LIST_SCHEMA: Incomplete
SERVICE_SORT_SCHEMA: Incomplete

@callback
def async_register_services(hass: HomeAssistant) -> None: ...
