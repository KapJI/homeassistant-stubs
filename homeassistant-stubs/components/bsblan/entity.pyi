from . import BSBLanData as BSBLanData
from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .coordinator import BSBLanCoordinator as BSBLanCoordinator, BSBLanFastCoordinator as BSBLanFastCoordinator, BSBLanSlowCoordinator as BSBLanSlowCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BSBLanEntityBase[_T: BSBLanCoordinator](CoordinatorEntity[_T]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _T, data: BSBLanData) -> None: ...

class BSBLanEntity(BSBLanEntityBase[BSBLanFastCoordinator]):
    def __init__(self, coordinator: BSBLanFastCoordinator, data: BSBLanData) -> None: ...

class BSBLanDualCoordinatorEntity(BSBLanEntity):
    slow_coordinator: Incomplete
    def __init__(self, fast_coordinator: BSBLanFastCoordinator, slow_coordinator: BSBLanSlowCoordinator, data: BSBLanData) -> None: ...
    async def async_added_to_hass(self) -> None: ...
