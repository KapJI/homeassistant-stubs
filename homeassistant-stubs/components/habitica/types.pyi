from .coordinator import HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type HabiticaConfigEntry = ConfigEntry[HabiticaDataUpdateCoordinator]
class HabiticaTaskType(StrEnum):
    HABIT = 'habit'
    DAILY = 'daily'
    TODO = 'todo'
    REWARD = 'reward'
