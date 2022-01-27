from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from bimmer_connected.remote_services import RemoteServiceStatus as RemoteServiceStatus
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class BMWButtonEntityDescription(ButtonEntityDescription):
    enabled_when_read_only: bool
    remote_function: Union[Callable[[ConnectedDriveVehicle], RemoteServiceStatus], None]
    account_function: Union[Callable[[BMWConnectedDriveAccount], None], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, enabled_when_read_only, remote_function, account_function) -> None: ...

BUTTON_TYPES: tuple[BMWButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWButton(BMWConnectedDriveBaseEntity, ButtonEntity):
    entity_description: BMWButtonEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle, description: BMWButtonEntityDescription) -> None: ...
    def press(self) -> None: ...
