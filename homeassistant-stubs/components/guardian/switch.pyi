from . import ValveControllerEntity as ValveControllerEntity
from .const import API_VALVE_STATUS as API_VALVE_STATUS, CONF_UID as CONF_UID, DATA_CLIENT as DATA_CLIENT, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PAIRED_SENSOR_MANAGER as DATA_PAIRED_SENSOR_MANAGER, DOMAIN as DOMAIN, LOGGER as LOGGER
from aioguardian import Client as Client
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FILENAME as CONF_FILENAME, CONF_PORT as CONF_PORT, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_AVG_CURRENT: str
ATTR_INST_CURRENT: str
ATTR_INST_CURRENT_DDT: str
ATTR_TRAVEL_COUNT: str
SERVICE_DISABLE_AP: str
SERVICE_ENABLE_AP: str
SERVICE_PAIR_SENSOR: str
SERVICE_REBOOT: str
SERVICE_RESET_VALVE_DIAGNOSTICS: str
SERVICE_UNPAIR_SENSOR: str
SERVICE_UPGRADE_FIRMWARE: str
SWITCH_KIND_VALVE: str
SWITCH_DESCRIPTION_VALVE: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValveControllerSwitch(ValveControllerEntity, SwitchEntity):
    _attr_is_on: bool
    _client: Any
    def __init__(self, entry: ConfigEntry, client: Client, coordinators: dict[str, DataUpdateCoordinator]) -> None: ...
    async def _async_continue_entity_setup(self) -> None: ...
    _attr_available: Any
    def _async_update_from_latest_data(self) -> None: ...
    async def async_disable_ap(self) -> None: ...
    async def async_enable_ap(self) -> None: ...
    async def async_pair_sensor(self, uid: str) -> None: ...
    async def async_reboot(self) -> None: ...
    async def async_reset_valve_diagnostics(self) -> None: ...
    async def async_unpair_sensor(self, uid: str) -> None: ...
    async def async_upgrade_firmware(self, url: str, port: int, filename: str) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
