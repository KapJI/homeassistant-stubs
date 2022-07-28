from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

class SensiboSelectDescriptionMixin:
    remote_key: str
    remote_options: str
    def __init__(self, remote_key, remote_options) -> None: ...

class SensiboSelectEntityDescription(SelectEntityDescription, SensiboSelectDescriptionMixin):
    def __init__(self, remote_key, remote_options, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

DEVICE_SELECT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboSelect(SensiboDeviceBaseEntity, SelectEntity):
    entity_description: SensiboSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
