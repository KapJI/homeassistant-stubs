from ..const import DOMAIN as DOMAIN
from ..mixins import async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .schema import CONF_SCHEMA as CONF_SCHEMA, LEGACY as LEGACY, MQTT_VACUUM_SCHEMA as MQTT_VACUUM_SCHEMA, STATE as STATE
from .schema_legacy import DISCOVERY_SCHEMA_LEGACY as DISCOVERY_SCHEMA_LEGACY, MqttVacuum as MqttVacuum, PLATFORM_SCHEMA_LEGACY_MODERN as PLATFORM_SCHEMA_LEGACY_MODERN
from .schema_state import DISCOVERY_SCHEMA_STATE as DISCOVERY_SCHEMA_STATE, MqttStateVacuum as MqttStateVacuum, PLATFORM_SCHEMA_STATE_MODERN as PLATFORM_SCHEMA_STATE_MODERN
from _typeshed import Incomplete
from homeassistant.components import vacuum as vacuum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
MQTT_VACUUM_DOCS_URL: str

def warn_for_deprecation_legacy_schema(hass: HomeAssistant, config: ConfigType, discovery: bool) -> None: ...
def validate_mqtt_vacuum_discovery(config_value: ConfigType) -> ConfigType: ...
def validate_mqtt_vacuum_modern(config_value: ConfigType) -> ConfigType: ...

DISCOVERY_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
