import abc
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from aiowithings import Activity, Goals, MeasurementType, NotificationCategory, SleepSummary, WithingsClient as WithingsClient, Workout
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import TypeVar

_T = TypeVar('_T')
UPDATE_INTERVAL: Incomplete

class WithingsDataUpdateCoordinator(DataUpdateCoordinator[_T], metaclass=abc.ABCMeta):
    config_entry: ConfigEntry
    _default_update_interval: timedelta | None
    _last_valid_update: datetime | None
    webhooks_connected: bool
    _client: Incomplete
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    update_interval: Incomplete
    def webhook_subscription_listener(self, connected: bool) -> None: ...
    async def async_webhook_data_updated(self, notification_category: NotificationCategory) -> None: ...
    async def _async_update_data(self) -> _T: ...
    @abstractmethod
    async def _internal_update_data(self) -> _T: ...

class WithingsMeasurementDataUpdateCoordinator(WithingsDataUpdateCoordinator[dict[MeasurementType, float]]):
    notification_categories: Incomplete
    _previous_data: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> dict[MeasurementType, float]: ...

class WithingsSleepDataUpdateCoordinator(WithingsDataUpdateCoordinator[SleepSummary | None]):
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    async def _internal_update_data(self) -> SleepSummary | None: ...

class WithingsBedPresenceDataUpdateCoordinator(WithingsDataUpdateCoordinator[None]):
    in_bed: bool | None
    _default_update_interval: Incomplete
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    async def async_webhook_data_updated(self, notification_category: NotificationCategory) -> None: ...
    async def _internal_update_data(self) -> None: ...

class WithingsGoalsDataUpdateCoordinator(WithingsDataUpdateCoordinator[Goals]):
    _default_update_interval: Incomplete
    def webhook_subscription_listener(self, connected: bool) -> None: ...
    async def _internal_update_data(self) -> Goals: ...

class WithingsActivityDataUpdateCoordinator(WithingsDataUpdateCoordinator[Activity | None]):
    _previous_data: Activity | None
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> Activity | None: ...

class WithingsWorkoutDataUpdateCoordinator(WithingsDataUpdateCoordinator[Workout | None]):
    _previous_data: Workout | None
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> Workout | None: ...
