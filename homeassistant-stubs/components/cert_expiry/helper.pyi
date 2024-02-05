import datetime
import ssl
from .const import TIMEOUT as TIMEOUT
from .errors import ConnectionRefused as ConnectionRefused, ConnectionTimeout as ConnectionTimeout, ResolveFailed as ResolveFailed, ValidationFailure as ValidationFailure
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

def _get_default_ssl_context() -> ssl.SSLContext: ...
async def async_get_cert(hass: HomeAssistant, host: str, port: int) -> dict[str, Any]: ...
async def get_cert_expiry_timestamp(hass: HomeAssistant, hostname: str, port: int) -> datetime.datetime: ...
