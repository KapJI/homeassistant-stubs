from .data import RestData as RestData
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import template as template
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
RestConfigEntry: Incomplete

class RestCoordinator(DataUpdateCoordinator[None]):
    rest: RestData
    def __init__(self, hass: HomeAssistant, rest: RestData, config_entry: RestConfigEntry | None, resource_template: template.Template | None, payload_template: template.Template | None, update_interval: timedelta) -> None: ...
