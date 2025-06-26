from .const import LOGGER as LOGGER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.template import Template as Template

_EXEC_FAILED_CODE: int

async def async_call_shell_with_timeout(command: str, timeout: int, *, log_return_code: bool = True) -> int: ...
async def async_check_output_or_log(command: str, timeout: int) -> str | None: ...
def render_template_args(hass: HomeAssistant, command: str) -> str | None: ...
