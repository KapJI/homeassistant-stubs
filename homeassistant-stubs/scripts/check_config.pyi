from homeassistant import core as core
from homeassistant.config import get_default_config_dir as get_default_config_dir
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.check_config import async_check_ha_config_file as async_check_ha_config_file
from homeassistant.util.yaml import Secrets as Secrets
from typing import Any, Callable, Optional

REQUIREMENTS: Any
_LOGGER: Any
MOCKS: dict[str, tuple[str, Callable]]
PATCHES: dict[str, Any]
C_HEAD: str
ERROR_STR: str

def color(the_color: Any, *args: Any, reset: Optional[Any] = ...): ...
def run(script_args: list) -> int: ...
def check(config_dir: Any, secrets: bool = ...): ...
async def async_check_config(config_dir: Any): ...
def line_info(obj: Any, **kwargs: Any): ...
def dump_dict(layer: Any, indent_count: int = ..., listi: bool = ..., **kwargs: Any): ...
