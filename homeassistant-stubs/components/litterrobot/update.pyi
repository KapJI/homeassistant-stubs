from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.start import async_at_start as async_at_start
from pylitterbot import LitterRobot4
from typing import Any

FIRMWARE_UPDATE_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RobotUpdateEntity(LitterRobotEntity[LitterRobot4], UpdateEntity):
    _attr_supported_features: Incomplete
    _poll_unsub: Incomplete
    def __init__(self, robot: LitterRobot4, hub: LitterRobotHub, description: UpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str: ...
    @property
    def in_progress(self) -> bool: ...
    _attr_latest_version: Incomplete
    async def _async_update(self, _: Union[HomeAssistant, datetime, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
