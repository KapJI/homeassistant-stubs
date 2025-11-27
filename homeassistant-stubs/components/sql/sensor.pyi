from .const import CONF_ADVANCED_OPTIONS as CONF_ADVANCED_OPTIONS, CONF_COLUMN_NAME as CONF_COLUMN_NAME, CONF_QUERY as CONF_QUERY, DOMAIN as DOMAIN
from .util import InvalidSqlQuery as InvalidSqlQuery, async_create_sessionmaker as async_create_sessionmaker, check_and_render_sql_query as check_and_render_sql_query, convert_value as convert_value, generate_lambda_stmt as generate_lambda_stmt, redact_credentials as redact_credentials, resolve_db_url as resolve_db_url, validate_query as validate_query
from _typeshed import Incomplete
from homeassistant.components.recorder import CONF_DB_URL as CONF_DB_URL, get_instance as get_instance
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady, TemplateError as TemplateError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerSensorEntity as ManualTriggerSensorEntity, ValueTemplate as ValueTemplate
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from sqlalchemy.engine import Result as Result
from sqlalchemy.orm import scoped_session as scoped_session
from typing import Any

_LOGGER: Incomplete
TRIGGER_ENTITY_OPTIONS: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
async def async_setup_sensor(hass: HomeAssistant, trigger_entity_config: ConfigType, query_template: ValueTemplate, column_name: str, value_template: ValueTemplate | None, unique_id: str | None, db_url: str, yaml: bool, async_add_entities: AddEntitiesCallback | AddConfigEntryEntitiesCallback) -> None: ...

class SQLSensor(ManualTriggerSensorEntity):
    _unrecorded_attributes: Incomplete
    _query: Incomplete
    _template: Incomplete
    _column_name: Incomplete
    sessionmaker: Incomplete
    _attr_extra_state_attributes: Incomplete
    _use_database_executor: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, trigger_entity_config: ConfigType, sessmaker: scoped_session, query: ValueTemplate, column: str, value_template: ValueTemplate | None, yaml: bool, use_database_executor: bool) -> None: ...
    @property
    def name(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def async_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _update(self) -> None: ...
