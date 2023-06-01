from ..mixins import async_setup_entry_helper as async_setup_entry_helper
from .schema import CONF_SCHEMA as CONF_SCHEMA, LEGACY as LEGACY, MQTT_VACUUM_SCHEMA as MQTT_VACUUM_SCHEMA, STATE as STATE
from .schema_legacy import DISCOVERY_SCHEMA_LEGACY as DISCOVERY_SCHEMA_LEGACY, PLATFORM_SCHEMA_LEGACY_MODERN as PLATFORM_SCHEMA_LEGACY_MODERN, async_setup_entity_legacy as async_setup_entity_legacy
from .schema_state import DISCOVERY_SCHEMA_STATE as DISCOVERY_SCHEMA_STATE, PLATFORM_SCHEMA_STATE_MODERN as PLATFORM_SCHEMA_STATE_MODERN, async_setup_entity_state as async_setup_entity_state
from _typeshed import Incomplete
from homeassistant.components import vacuum as vacuum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

def validate_mqtt_vacuum_discovery(config_value: ConfigType) -> ConfigType: ...
def validate_mqtt_vacuum_modern(config_value: ConfigType) -> ConfigType: ...

DISCOVERY_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...
