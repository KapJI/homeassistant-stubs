from homeassistant.components.frontend import EVENT_PANELS_UPDATED as EVENT_PANELS_UPDATED
from homeassistant.components.lovelace.const import EVENT_LOVELACE_UPDATED as EVENT_LOVELACE_UPDATED
from homeassistant.components.persistent_notification import EVENT_PERSISTENT_NOTIFICATIONS_UPDATED as EVENT_PERSISTENT_NOTIFICATIONS_UPDATED
from homeassistant.const import EVENT_COMPONENT_LOADED as EVENT_COMPONENT_LOADED, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, EVENT_SERVICE_REGISTERED as EVENT_SERVICE_REGISTERED, EVENT_SERVICE_REMOVED as EVENT_SERVICE_REMOVED, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, EVENT_THEMES_UPDATED as EVENT_THEMES_UPDATED
from homeassistant.helpers.area_registry import EVENT_AREA_REGISTRY_UPDATED as EVENT_AREA_REGISTRY_UPDATED
from homeassistant.helpers.device_registry import EVENT_DEVICE_REGISTRY_UPDATED as EVENT_DEVICE_REGISTRY_UPDATED
from homeassistant.helpers.entity_registry import EVENT_ENTITY_REGISTRY_UPDATED as EVENT_ENTITY_REGISTRY_UPDATED
from typing import Final

SUBSCRIBE_ALLOWLIST: Final[set[str]]
