from _typeshed import Incomplete
from homeassistant import core as core
from homeassistant.helpers.device_registry import format_mac as format_mac
from pyialarmxr import IAlarmXR as IAlarmXR

_LOGGER: Incomplete

async def async_get_ialarmxr_mac(hass: core.HomeAssistant, ialarmxr: IAlarmXR) -> str: ...
