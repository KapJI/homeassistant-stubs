from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.util import decorator as decorator
from homeassistant.util.yaml.dumper import add_representer as add_representer, represent_odict as represent_odict
from typing import Any, TypedDict

SELECTORS: decorator.Registry[str, type[Selector]]

def _get_selector_class(config: Any) -> type[Selector]: ...
def selector(config: Any) -> Selector: ...
def validate_selector(config: Any) -> dict: ...

class Selector:
    CONFIG_SCHEMA: Callable
    config: Any
    selector_type: str
    def __init__(self, config: Any = ...) -> None: ...
    def serialize(self) -> Any: ...

SINGLE_ENTITY_SELECTOR_CONFIG_SCHEMA: Incomplete

class SingleEntitySelectorConfig(TypedDict):
    integration: str
    domain: str
    device_class: str

SINGLE_DEVICE_SELECTOR_CONFIG_SCHEMA: Incomplete

class SingleDeviceSelectorConfig(TypedDict):
    integration: str
    manufacturer: str
    model: str
    entity: SingleEntitySelectorConfig

class ActionSelectorConfig(TypedDict): ...

class ActionSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[ActionSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class AddonSelectorConfig(TypedDict):
    name: str
    slug: str

class AddonSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[AddonSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...

class AreaSelectorConfig(TypedDict):
    entity: SingleEntitySelectorConfig
    device: SingleDeviceSelectorConfig
    multiple: bool

class AreaSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[AreaSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class AttributeSelectorConfig(TypedDict):
    entity_id: str

class AttributeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: AttributeSelectorConfig) -> None: ...
    def __call__(self, data: Any) -> str: ...

class BooleanSelectorConfig(TypedDict): ...

class BooleanSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[BooleanSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> bool: ...

class ColorRGBSelectorConfig(TypedDict): ...

class ColorRGBSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[ColorRGBSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> list[int]: ...

class ColorTempSelectorConfig(TypedDict):
    max_mireds: int
    min_mireds: int

class ColorTempSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[ColorTempSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> int: ...

class DateSelectorConfig(TypedDict): ...

class DateSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[DateSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class DateTimeSelectorConfig(TypedDict): ...

class DateTimeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[DateTimeSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class DeviceSelectorConfig(TypedDict):
    integration: str
    manufacturer: str
    model: str
    entity: SingleEntitySelectorConfig
    multiple: bool

class DeviceSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[DeviceSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class DurationSelectorConfig(TypedDict):
    enable_day: bool

class DurationSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[DurationSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class EntitySelectorConfig(SingleEntitySelectorConfig):
    exclude_entities: list[str]
    include_entities: list[str]
    multiple: bool

class EntitySelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[EntitySelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Union[str, list[str]]: ...

class IconSelectorConfig(TypedDict):
    placeholder: str

class IconSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[IconSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...

class LocationSelectorConfig(TypedDict):
    radius: bool
    icon: str

class LocationSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    DATA_SCHEMA: Incomplete
    def __init__(self, config: Union[LocationSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class MediaSelectorConfig(TypedDict): ...

class MediaSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    DATA_SCHEMA: Incomplete
    def __init__(self, config: Union[MediaSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> dict[str, float]: ...

class NumberSelectorConfig(TypedDict):
    min: float
    max: float
    step: float
    unit_of_measurement: str
    mode: NumberSelectorMode

class NumberSelectorMode(StrEnum):
    BOX: str
    SLIDER: str

def has_min_max_if_slider(data: Any) -> Any: ...

class NumberSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[NumberSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> float: ...

class ObjectSelectorConfig(TypedDict): ...

class ObjectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[ObjectSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Any: ...

select_option: Incomplete

class SelectOptionDict(TypedDict):
    value: str
    label: str

class SelectSelectorMode(StrEnum):
    LIST: str
    DROPDOWN: str

class SelectSelectorConfig(TypedDict):
    options: Union[Sequence[SelectOptionDict], Sequence[str]]
    multiple: bool
    custom_value: bool
    mode: SelectSelectorMode

class SelectSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[SelectSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class TargetSelectorConfig(TypedDict):
    entity: SingleEntitySelectorConfig
    device: SingleDeviceSelectorConfig

class TargetSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    TARGET_SELECTION_SCHEMA: Incomplete
    def __init__(self, config: Union[TargetSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> dict[str, list[str]]: ...

class TemplateSelectorConfig(TypedDict): ...

class TemplateSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[TemplateSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TextSelectorConfig(TypedDict):
    multiline: bool
    suffix: str
    type: TextSelectorType

class TextSelectorType(StrEnum):
    COLOR: str
    DATE: str
    DATETIME_LOCAL: str
    EMAIL: str
    MONTH: str
    NUMBER: str
    PASSWORD: str
    SEARCH: str
    TEL: str
    TEXT: str
    TIME: str
    URL: str
    WEEK: str

class TextSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[TextSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...

class ThemeSelectorConfig(TypedDict): ...

class ThemeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[ThemeSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...

class TimeSelectorConfig(TypedDict): ...

class TimeSelector(Selector):
    selector_type: str
    CONFIG_SCHEMA: Incomplete
    def __init__(self, config: Union[TimeSelectorConfig, None] = ...) -> None: ...
    def __call__(self, data: Any) -> str: ...
