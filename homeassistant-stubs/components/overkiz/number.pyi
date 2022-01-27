from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class OverkizNumberDescriptionMixin:
    command: str
    def __init__(self, command) -> None: ...

class OverkizNumberDescription(NumberEntityDescription, OverkizNumberDescriptionMixin):
    def __init__(self, command, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step) -> None: ...

NUMBER_DESCRIPTIONS: list[OverkizNumberDescription]
SUPPORTED_STATES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizNumber(OverkizDescriptiveEntity, NumberEntity):
    entity_description: OverkizNumberDescription
    @property
    def value(self) -> Union[float, None]: ...
    async def async_set_value(self, value: float) -> None: ...
