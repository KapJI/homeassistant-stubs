import logging
from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, OAuth2TokenRequestError as OAuth2TokenRequestError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.decorator import Registry as Registry
from pyoverkiz.client import OverkizClient as OverkizClient
from pyoverkiz.models import Device, DeviceEvent as DeviceEvent, DeviceRemovedEvent as DeviceRemovedEvent, DeviceStateChangedEvent as DeviceStateChangedEvent, ExecutionRegisteredEvent as ExecutionRegisteredEvent, ExecutionStateChangedEvent as ExecutionStateChangedEvent, Place
from typing import Any, override

EVENT_HANDLERS: Registry[str, Callable[[OverkizDataUpdateCoordinator, Any], Coroutine[Any, Any, None]]]

class OverkizDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Device]]):
    config_entry: OverkizDataConfigEntry
    _default_update_interval: timedelta
    data: Incomplete
    client: Incomplete
    devices: dict[str, Device]
    executions: dict[str, list[dict[str, str]]]
    areas: Incomplete
    is_stateless: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OverkizDataConfigEntry, logger: logging.Logger, *, client: OverkizClient, devices: list[Device], places: Place | None) -> None: ...
    update_interval: Incomplete
    @override
    async def _async_update_data(self) -> dict[str, Device]: ...
    async def _get_devices(self) -> dict[str, Device]: ...
    def _places_to_area(self, place: Place) -> dict[str, str]: ...
    def set_update_interval(self, update_interval: timedelta) -> None: ...

async def on_device_available(coordinator: OverkizDataUpdateCoordinator, event: DeviceEvent) -> None: ...
async def on_device_unavailable_disabled(coordinator: OverkizDataUpdateCoordinator, event: DeviceEvent) -> None: ...
async def on_device_created_updated(coordinator: OverkizDataUpdateCoordinator, event: DeviceEvent) -> None: ...
async def on_device_state_changed(coordinator: OverkizDataUpdateCoordinator, event: DeviceStateChangedEvent) -> None: ...
async def on_device_removed(coordinator: OverkizDataUpdateCoordinator, event: DeviceRemovedEvent) -> None: ...
async def on_execution_registered(coordinator: OverkizDataUpdateCoordinator, event: ExecutionRegisteredEvent) -> None: ...
async def on_execution_state_changed(coordinator: OverkizDataUpdateCoordinator, event: ExecutionStateChangedEvent) -> None: ...
