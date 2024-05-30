from .const import DOMAIN as DOMAIN
from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from .models import DomainData as DomainData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from sfrbox_api.models import DslInfo, FtthInfo, SystemInfo as SystemInfo, WanInfo

@dataclass(frozen=True, kw_only=True)
class SFRBoxBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[_T], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

DSL_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[DslInfo], ...]
FTTH_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[FtthInfo], ...]
WAN_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[WanInfo], ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SFRBoxBinarySensor(CoordinatorEntity[SFRDataUpdateCoordinator[_T]], BinarySensorEntity):
    entity_description: SFRBoxBinarySensorEntityDescription[_T]
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SFRDataUpdateCoordinator[_T], description: SFRBoxBinarySensorEntityDescription, system_info: SystemInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
