from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import AmazonDevicesCoordinator as AmazonDevicesCoordinator
from aioamazondevices.structures import AmazonDevice as AmazonDevice
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_update_unique_id(hass: HomeAssistant, coordinator: AmazonDevicesCoordinator, platform: str, old_key: str, new_key: str) -> None: ...
async def async_remove_entities(hass: HomeAssistant, coordinator: AmazonDevicesCoordinator, platform: str, key: str, remove_fn: Callable[[AmazonDevice], bool]) -> None: ...
async def async_remove_unsupported_notification_sensors(hass: HomeAssistant, coordinator: AmazonDevicesCoordinator) -> None: ...
