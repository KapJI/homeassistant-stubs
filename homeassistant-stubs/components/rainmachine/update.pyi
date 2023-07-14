from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity
from .const import DATA_MACHINE_FIRMWARE_UPDATE_STATUS as DATA_MACHINE_FIRMWARE_UPDATE_STATUS, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription
from _typeshed import Incomplete
from enum import Enum
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class UpdateStates(Enum):
    IDLE: int
    CHECKING: int
    DOWNLOADING: int
    UPGRADING: int
    ERROR: int
    REBOOT: int

UPDATE_STATE_MAP: Incomplete
UPDATE_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineUpdateEntity(RainMachineEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_in_progress: bool
    _attr_latest_version: Incomplete
    _attr_title: Incomplete
    def update_from_latest_data(self) -> None: ...
