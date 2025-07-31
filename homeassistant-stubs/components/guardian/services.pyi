from . import GuardianConfigEntry as GuardianConfigEntry, GuardianData as GuardianData
from .const import CONF_UID as CONF_UID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_FILENAME as CONF_FILENAME, CONF_PORT as CONF_PORT, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

SERVICE_NAME_PAIR_SENSOR: str
SERVICE_NAME_UNPAIR_SENSOR: str
SERVICE_NAME_UPGRADE_FIRMWARE: str
SERVICES: Incomplete
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_PAIR_UNPAIR_SENSOR_SCHEMA: Incomplete
SERVICE_UPGRADE_FIRMWARE_SCHEMA: Incomplete

@callback
def async_get_entry_id_for_service_call(call: ServiceCall) -> GuardianConfigEntry: ...
@callback
def call_with_data(func: Callable[[ServiceCall, GuardianData], Coroutine[Any, Any, None]]) -> Callable[[ServiceCall], Coroutine[Any, Any, None]]: ...
@call_with_data
async def async_pair_sensor(call: ServiceCall, data: GuardianData) -> None: ...
@call_with_data
async def async_unpair_sensor(call: ServiceCall, data: GuardianData) -> None: ...
@call_with_data
async def async_upgrade_firmware(call: ServiceCall, data: GuardianData) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
