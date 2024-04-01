from .const import DOMAIN as DOMAIN
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

@dataclass(frozen=True, kw_only=True)
class RenaultSelectEntityDescription(SelectEntityDescription, RenaultDataEntityDescription):
    data_key: str
    def __init__(self, coordinator, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, data_key) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultSelectEntity(RenaultDataEntity[KamereonVehicleBatteryStatusData], SelectEntity):
    entity_description: RenaultSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    @property
    def data(self) -> StateType: ...
    async def async_select_option(self, option: str) -> None: ...

SENSOR_TYPES: tuple[RenaultSelectEntityDescription, ...]
