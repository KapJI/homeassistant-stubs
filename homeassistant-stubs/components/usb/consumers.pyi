from .const import DOMAIN as DOMAIN
from .models import SerialDevice as SerialDevice, SerialPortConsumer as SerialPortConsumer, USBDevice as USBDevice
from _typeshed import Incomplete
from collections.abc import Iterator, Mapping, Sequence
from homeassistant.components.hassio import HassioNotReadyError as HassioNotReadyError, get_addons_info as get_addons_info
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.hassio import is_hassio as is_hassio
from homeassistant.loader import async_get_integrations as async_get_integrations
from typing import Any

SERIAL_PORT_KEY_PATHS: tuple[tuple[str, ...], ...]
NON_USB_SERIAL_DOMAINS: Incomplete
ACTIVE_CONFIG_ENTRY_STATES: Incomplete
SCANNED_PORT_SCHEMES: Incomplete
UNSCANNABLE_PORT_SCHEMES: Incomplete
BAUD_SUFFIX_RE: Incomplete
APP_STATE_STARTED: str

def _resolve_key_path(data: Mapping[str, Any], key_path: tuple[str, ...]) -> Any: ...
def _serial_port_from_value(value: Any, known_devices: set[str], domain: str) -> str | None: ...
def _resolve_paths(paths: set[str]) -> dict[str, str]: ...
async def _async_get_config_entry_consumers(hass: HomeAssistant, known_devices: set[str]) -> dict[str, list[SerialPortConsumer]]: ...
def _iter_option_device_paths(value: Any) -> Iterator[str]: ...
@callback
def _async_get_app_consumers(hass: HomeAssistant) -> dict[str, list[SerialPortConsumer]]: ...
async def async_get_serial_port_consumers(hass: HomeAssistant, ports: Sequence[USBDevice | SerialDevice]) -> dict[str, list[SerialPortConsumer]]: ...
