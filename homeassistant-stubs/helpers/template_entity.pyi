import voluptuous as vol
from .entity import Entity as Entity
from .event import TrackTemplate as TrackTemplate, TrackTemplateResult as TrackTemplateResult, async_track_template_result as async_track_template_result
from .script import Script as Script, _VarsType as _VarsType
from .template import Template as Template, TemplateStateFromEntityId as TemplateStateFromEntityId, render_complex as render_complex, result_as_boolean as result_as_boolean
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Context as Context, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any

_LOGGER: Incomplete
CONF_AVAILABILITY: str
CONF_ATTRIBUTES: str
CONF_PICTURE: str
CONF_TO_ATTRIBUTE: Incomplete
TEMPLATE_ENTITY_BASE_SCHEMA: Incomplete

def make_template_entity_base_schema(default_name: str) -> vol.Schema: ...

TEMPLATE_SENSOR_BASE_SCHEMA: Incomplete

class _TemplateAttribute:
    _entity: Incomplete
    _attribute: Incomplete
    template: Incomplete
    validator: Incomplete
    on_update: Incomplete
    async_update: Incomplete
    none_on_template_error: Incomplete
    def __init__(self, entity: Entity, attribute: str, template: Template, validator: Callable[[Any], Any] | None = ..., on_update: Callable[[Any], None] | None = ..., none_on_template_error: bool | None = ...) -> None: ...
    def async_setup(self) -> None: ...
    def _default_update(self, result: str | TemplateError) -> None: ...
    def handle_result(self, event: Event | None, template: Template, last_result: str | None | TemplateError, result: str | TemplateError) -> None: ...

class TemplateEntity(Entity):
    _attr_available: bool
    _attr_entity_picture: Incomplete
    _attr_icon: Incomplete
    _template_attrs: Incomplete
    _async_update: Incomplete
    _attr_extra_state_attributes: Incomplete
    _self_ref_update_count: int
    _attr_unique_id: Incomplete
    _attribute_templates: Incomplete
    _availability_template: Incomplete
    _icon_template: Incomplete
    _entity_picture_template: Incomplete
    _friendly_name_template: Incomplete
    entity_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, hass: HomeAssistant, *, availability_template: Template | None = ..., icon_template: Template | None = ..., entity_picture_template: Template | None = ..., attribute_templates: dict[str, Template] | None = ..., config: ConfigType | None = ..., fallback_name: str | None = ..., unique_id: str | None = ...) -> None: ...
    def _update_available(self, result: str | TemplateError) -> None: ...
    def _update_state(self, result: str | TemplateError) -> None: ...
    def _add_attribute_template(self, attribute_key: str, attribute_template: Template) -> None: ...
    def add_template_attribute(self, attribute: str, template: Template, validator: Callable[[Any], Any] | None = ..., on_update: Callable[[Any], None] | None = ..., none_on_template_error: bool = ...) -> None: ...
    def _handle_results(self, event: Event | None, updates: list[TrackTemplateResult]) -> None: ...
    async def _async_template_startup(self, *_: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_run_script(self, script: Script, *, run_variables: _VarsType | None = ..., context: Context | None = ...) -> None: ...

class TemplateSensor(TemplateEntity, SensorEntity):
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, hass: HomeAssistant, *, config: dict[str, Any], fallback_name: str | None, unique_id: str | None) -> None: ...

class TriggerBaseEntity(Entity):
    domain: str
    extra_template_keys: tuple | None
    extra_template_keys_complex: tuple | None
    _unique_id: str | None
    hass: Incomplete
    _config: Incomplete
    _static_rendered: Incomplete
    _to_render_simple: Incomplete
    _to_render_complex: Incomplete
    _rendered: Incomplete
    _parse_result: Incomplete
    def __init__(self, hass: HomeAssistant, config: dict) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def device_class(self): ...
    @property
    def icon(self) -> str | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def async_added_to_hass(self) -> None: ...
    def _set_unique_id(self, unique_id: str | None) -> None: ...
    def restore_attributes(self, last_state: State) -> None: ...
    def _render_templates(self, variables: dict[str, Any]) -> None: ...

class ManualTriggerEntity(TriggerBaseEntity):
    def __init__(self, hass: HomeAssistant, config: dict) -> None: ...
    def _process_manual_data(self, value: str | None = ...) -> None: ...
