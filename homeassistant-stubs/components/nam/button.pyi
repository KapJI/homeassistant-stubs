from . import NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Any
RESTART_BUTTON: ButtonEntityDescription

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NAMButton(CoordinatorEntity, ButtonEntity):
    coordinator: NAMDataUpdateCoordinator
    _attr_device_info: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, coordinator: NAMDataUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
