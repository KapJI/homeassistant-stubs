from ..mixins import async_setup_entry_helper as async_setup_entry_helper
from .schema import CONF_SCHEMA as CONF_SCHEMA, MQTT_LIGHT_SCHEMA_SCHEMA as MQTT_LIGHT_SCHEMA_SCHEMA
from .schema_basic import DISCOVERY_SCHEMA_BASIC as DISCOVERY_SCHEMA_BASIC, PLATFORM_SCHEMA_MODERN_BASIC as PLATFORM_SCHEMA_MODERN_BASIC, async_setup_entity_basic as async_setup_entity_basic
from .schema_json import DISCOVERY_SCHEMA_JSON as DISCOVERY_SCHEMA_JSON, PLATFORM_SCHEMA_MODERN_JSON as PLATFORM_SCHEMA_MODERN_JSON, async_setup_entity_json as async_setup_entity_json
from .schema_template import DISCOVERY_SCHEMA_TEMPLATE as DISCOVERY_SCHEMA_TEMPLATE, PLATFORM_SCHEMA_MODERN_TEMPLATE as PLATFORM_SCHEMA_MODERN_TEMPLATE, async_setup_entity_template as async_setup_entity_template
from _typeshed import Incomplete
from homeassistant.components import light as light
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

def validate_mqtt_light_discovery(config_value: dict[str, Any]) -> ConfigType: ...
def validate_mqtt_light_modern(config_value: dict[str, Any]) -> ConfigType: ...

DISCOVERY_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...
