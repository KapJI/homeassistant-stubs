from asyncsleepiq import AsyncSleepIQ as AsyncSleepIQ
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Any
UPDATE_INTERVAL: Any
LONGER_UPDATE_INTERVAL: Any

class SleepIQDataUpdateCoordinator(DataUpdateCoordinator[None]):
    client: Any
    def __init__(self, hass: HomeAssistant, client: AsyncSleepIQ, username: str) -> None: ...
    async def _async_update_data(self) -> None: ...

class SleepIQPauseUpdateCoordinator(DataUpdateCoordinator[None]):
    client: Any
    def __init__(self, hass: HomeAssistant, client: AsyncSleepIQ, username: str) -> None: ...
    async def _async_update_data(self) -> None: ...

class SleepIQData:
    data_coordinator: SleepIQDataUpdateCoordinator
    pause_coordinator: SleepIQPauseUpdateCoordinator
    client: AsyncSleepIQ
    def __init__(self, data_coordinator, pause_coordinator, client) -> None: ...
