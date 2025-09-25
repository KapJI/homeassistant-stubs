from .const import DOMAIN as DOMAIN, ENTRY_TITLE as ENTRY_TITLE
from _typeshed import Incomplete
from homeassistant.components.usb import get_serial_by_id as get_serial_by_id, human_readable_device_name as human_readable_device_name
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_ID as CONF_ID, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import callback as callback
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo
from typing import Any

_LOGGER: Incomplete

def _validate_input(device: str, id: str, password: str) -> None: ...
def _human_readable_device_name(port: UsbServiceInfo | ListPortInfo) -> str: ...

class BRouteConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    device: UsbServiceInfo | None
    @callback
    def _get_discovered_device_id_and_name(self, device_options: dict[str, ListPortInfo]) -> tuple[str | None, str | None]: ...
    async def _get_usb_devices(self) -> dict[str, ListPortInfo]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
