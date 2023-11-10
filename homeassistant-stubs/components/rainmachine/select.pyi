from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity
from .const import DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey as RainMachineEntityDescriptionMixinDataKey
from .util import key_exists as key_exists
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM, UnitSystem as UnitSystem

@dataclass
class RainMachineSelectDescription(SelectEntityDescription, RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey):
    def __init__(self, data_key, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options) -> None: ...

@dataclass
class FreezeProtectionSelectOption:
    api_value: float
    imperial_label: str
    metric_label: str
    def __init__(self, api_value, imperial_label, metric_label) -> None: ...

@dataclass
class FreezeProtectionTemperatureMixin:
    extended_options: list[FreezeProtectionSelectOption]
    def __init__(self, extended_options) -> None: ...

@dataclass
class FreezeProtectionSelectDescription(RainMachineSelectDescription, FreezeProtectionTemperatureMixin):
    def __init__(self, extended_options, data_key, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options) -> None: ...

TYPE_FREEZE_PROTECTION_TEMPERATURE: str
SELECT_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FreezeProtectionTemperatureSelect(RainMachineEntity, SelectEntity):
    entity_description: FreezeProtectionSelectDescription
    _api_value_to_label_map: Incomplete
    _label_to_api_value_map: Incomplete
    _attr_options: Incomplete
    def __init__(self, entry: ConfigEntry, data: RainMachineData, description: FreezeProtectionSelectDescription, unit_system: UnitSystem) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    def update_from_latest_data(self) -> None: ...
