import voluptuous as vol
from .entity import Entity as Entity
from .template import Template as Template, TemplateStateFromEntityId as TemplateStateFromEntityId, _SENTINEL as _SENTINEL, _render_with_context as _render_with_context, render_complex as render_complex, result_as_boolean as result_as_boolean
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.const import ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any

CONF_AVAILABILITY: str
CONF_ATTRIBUTES: str
CONF_PICTURE: str
CONF_TO_ATTRIBUTE: Incomplete
TEMPLATE_ENTITY_BASE_SCHEMA: Incomplete

def make_template_entity_base_schema(default_name: str) -> vol.Schema: ...
def log_triggered_template_error(entity_id: str, err: TemplateError, key: str | None = None, attribute: str | None = None) -> None: ...

TEMPLATE_SENSOR_BASE_SCHEMA: Incomplete

class ValueTemplate(Template):
    @classmethod
    def from_template(cls, template: Template) -> ValueTemplate: ...
    @callback
    def async_render_as_value_template(self, entity_id: str, variables: dict[str, Any], error_value: Any) -> Any: ...

class TriggerBaseEntity(Entity):
    domain: str
    extra_template_keys: tuple[str, ...] | None
    extra_template_keys_complex: tuple[str, ...] | None
    _unique_id: str | None
    hass: Incomplete
    _config: Incomplete
    _static_rendered: Incomplete
    _to_render_simple: list[str]
    _to_render_complex: list[str]
    _rendered: Incomplete
    _parse_result: Incomplete
    _attr_device_class: Incomplete
    _availability_template: Incomplete
    _available: bool
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def _set_unique_id(self, unique_id: str | None) -> None: ...
    def restore_attributes(self, last_state: State) -> None: ...
    def _template_variables(self, run_variables: dict[str, Any] | None = None) -> dict: ...
    def _render_single_template(self, key: str, variables: dict[str, Any], strict: bool = False) -> Any: ...
    def _render_availability_template(self, variables: dict[str, Any]) -> bool: ...
    def _render_attributes(self, rendered: dict, variables: dict[str, Any]) -> None: ...
    def _render_single_templates(self, rendered: dict, variables: dict[str, Any], filtered: list[str] | None = None) -> None: ...
    def _render_templates(self, variables: dict[str, Any]) -> None: ...

class ManualTriggerEntity(TriggerBaseEntity):
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    def _template_variables_with_value(self, value: str | None = None) -> dict[str, Any]: ...
    @callback
    def _process_manual_data(self, variables: dict[str, Any]) -> None: ...

class ManualTriggerSensorEntity(ManualTriggerEntity, SensorEntity):
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _set_native_value_with_possible_timestamp(self, value: Any) -> None: ...
