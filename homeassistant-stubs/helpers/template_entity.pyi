from .entity import Entity as Entity
from .event import TrackTemplate as TrackTemplate, TrackTemplateResult as TrackTemplateResult, async_track_template_result as async_track_template_result
from .script import Script as Script, _VarsType as _VarsType
from .template import Template as Template, TemplateStateFromEntityId as TemplateStateFromEntityId, result_as_boolean as result_as_boolean
from .typing import ConfigType as ConfigType
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Context as Context, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from typing import Any

_LOGGER: Incomplete
CONF_AVAILABILITY: str
CONF_ATTRIBUTES: str
CONF_PICTURE: str
TEMPLATE_ENTITY_BASE_SCHEMA: Incomplete
TEMPLATE_SENSOR_BASE_SCHEMA: Incomplete

class _TemplateAttribute:
    _entity: Incomplete
    _attribute: Incomplete
    template: Incomplete
    validator: Incomplete
    on_update: Incomplete
    async_update: Incomplete
    none_on_template_error: Incomplete
    def __init__(self, entity: Entity, attribute: str, template: Template, validator: Union[Callable[[Any], Any], None] = ..., on_update: Union[Callable[[Any], None], None] = ..., none_on_template_error: Union[bool, None] = ...) -> None: ...
    def async_setup(self) -> None: ...
    def _default_update(self, result: Union[str, TemplateError]) -> None: ...
    def handle_result(self, event: Union[Event, None], template: Template, last_result: Union[str, None, TemplateError], result: Union[str, TemplateError]) -> None: ...

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
    def __init__(self, hass: HomeAssistant, *, availability_template: Union[Template, None] = ..., icon_template: Union[Template, None] = ..., entity_picture_template: Union[Template, None] = ..., attribute_templates: Union[dict[str, Template], None] = ..., config: Union[ConfigType, None] = ..., fallback_name: Union[str, None] = ..., unique_id: Union[str, None] = ...) -> None: ...
    def _update_available(self, result: Union[str, TemplateError]) -> None: ...
    def _update_state(self, result: Union[str, TemplateError]) -> None: ...
    def _add_attribute_template(self, attribute_key: str, attribute_template: Template) -> None: ...
    def add_template_attribute(self, attribute: str, template: Template, validator: Union[Callable[[Any], Any], None] = ..., on_update: Union[Callable[[Any], None], None] = ..., none_on_template_error: bool = ...) -> None: ...
    def _handle_results(self, event: Union[Event, None], updates: list[TrackTemplateResult]) -> None: ...
    async def _async_template_startup(self, *_: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    async def async_run_script(self, script: Script, *, run_variables: Union[_VarsType, None] = ..., context: Union[Context, None] = ...) -> None: ...

class TemplateSensor(TemplateEntity, SensorEntity):
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, hass: HomeAssistant, *, config: dict[str, Any], fallback_name: Union[str, None], unique_id: Union[str, None]) -> None: ...
