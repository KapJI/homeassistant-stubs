from . import template as template
from collections.abc import Mapping
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class ScriptVariables:
    variables: Any
    _has_template: Any
    def __init__(self, variables: dict[str, Any]) -> None: ...
    def async_render(self, hass: HomeAssistant, run_variables: Union[Mapping[str, Any], None], *, render_as_defaults: bool = ..., limited: bool = ...) -> dict[str, Any]: ...
    def as_dict(self) -> dict: ...
