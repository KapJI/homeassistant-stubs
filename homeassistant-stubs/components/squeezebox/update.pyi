from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import DOMAIN as DOMAIN, SERVER_MODEL as SERVER_MODEL, STATUS_QUERY_VERSION as STATUS_QUERY_VERSION, STATUS_UPDATE_NEWPLUGINS as STATUS_UPDATE_NEWPLUGINS, STATUS_UPDATE_NEWVERSION as STATUS_UPDATE_NEWVERSION, UPDATE_PLUGINS_RELEASE_SUMMARY as UPDATE_PLUGINS_RELEASE_SUMMARY, UPDATE_RELEASE_SUMMARY as UPDATE_RELEASE_SUMMARY
from .entity import LMSStatusEntity as LMSStatusEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any

newserver: Incomplete
newplugins: Incomplete
POLL_AFTER_INSTALL: int
PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ServerStatusUpdate(LMSStatusEntity, UpdateEntity):
    @property
    def latest_version(self) -> str: ...

class ServerStatusUpdateLMS(ServerStatusUpdate):
    title: str
    @property
    def installed_version(self) -> str: ...
    @property
    def release_url(self) -> str: ...
    @property
    def release_summary(self) -> None | str: ...

class ServerStatusUpdatePlugins(ServerStatusUpdate):
    auto_update: bool
    title: str
    installed_version: str
    restart_triggered: bool
    _cancel_update: Callable | None
    @property
    def supported_features(self) -> UpdateEntityFeature: ...
    @property
    def release_summary(self) -> None | str: ...
    @property
    def release_url(self) -> str: ...
    @property
    def in_progress(self) -> bool: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def _async_update_catchall(self, now: datetime | None = None) -> None: ...
