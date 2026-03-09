from _typeshed import Incomplete
from asyncsleepiq import AsyncSleepIQ as AsyncSleepIQ
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
LONGER_UPDATE_INTERVAL: Incomplete
SLEEP_DATA_UPDATE_INTERVAL: Incomplete

class SleepIQDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: AsyncSleepIQ) -> None: ...
    async def _async_update_data(self) -> None: ...

class SleepIQPauseUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: AsyncSleepIQ) -> None: ...
    async def _async_update_data(self) -> None: ...

class SleepIQSleepDataCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: AsyncSleepIQ) -> None: ...
    async def _async_update_data(self) -> None: ...

@dataclass
class SleepIQData:
    data_coordinator: SleepIQDataUpdateCoordinator
    pause_coordinator: SleepIQPauseUpdateCoordinator
    sleep_data_coordinator: SleepIQSleepDataCoordinator
    client: AsyncSleepIQ
