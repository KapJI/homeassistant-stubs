from .const import DOMAIN as DOMAIN
from .controller import OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSiteController as OmadaSiteController
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client.devices import OmadaDevice as OmadaDevice, OmadaGateway, OmadaGatewayPort as OmadaGatewayPort

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_gateway_port_status_sensors(gateway: OmadaGateway, hass: HomeAssistant, coordinator: OmadaGatewayCoordinator) -> Generator[BinarySensorEntity, None, None]: ...

class GatewayPortBinarySensorConfig:
    port_number: int
    id_suffix: str
    name_suffix: str
    device_class: BinarySensorDeviceClass
    update_func: Callable[[OmadaGatewayPort], bool]
    def __init__(self, port_number, id_suffix, name_suffix, device_class, update_func) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class OmadaGatewayPortBinarySensor(OmadaDeviceEntity[OmadaGateway], BinarySensorEntity):
    _attr_has_entity_name: bool
    _config: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: OmadaGatewayCoordinator, device: OmadaDevice, config: GatewayPortBinarySensorConfig) -> None: ...
    _attr_is_on: Incomplete
    _attr_available: bool
    def _handle_coordinator_update(self) -> None: ...
