from .const import DOMAIN as DOMAIN
from .controller import OmadaGatewayCoordinator as OmadaGatewayCoordinator, OmadaSiteController as OmadaSiteController
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client.devices import OmadaDevice as OmadaDevice, OmadaGatewayPortConfig as OmadaGatewayPortConfig, OmadaGatewayPortStatus as OmadaGatewayPortStatus

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class GatewayPortBinarySensorEntityDescription(BinarySensorEntityDescription):
    exists_func: Callable[[OmadaGatewayPortConfig], bool] = ...
    update_func: Callable[[OmadaGatewayPortStatus], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, exists_func, update_func) -> None: ...

GATEWAY_PORT_SENSORS: list[GatewayPortBinarySensorEntityDescription]

class OmadaGatewayPortBinarySensor(OmadaDeviceEntity[OmadaGatewayCoordinator], BinarySensorEntity):
    entity_description: GatewayPortBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _port_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: OmadaGatewayCoordinator, device: OmadaDevice, port_number: int, entity_description: GatewayPortBinarySensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    def _do_update(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
