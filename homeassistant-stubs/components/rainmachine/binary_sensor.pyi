from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity
from .const import DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey as RainMachineEntityDescriptionMixinDataKey
from .util import EntityDomainReplacementStrategy as EntityDomainReplacementStrategy, async_finish_entity_domain_replacements as async_finish_entity_domain_replacements, key_exists as key_exists
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_FLOW_SENSOR: str
TYPE_FREEZE: str
TYPE_HOURLY: str
TYPE_MONTH: str
TYPE_RAINDELAY: str
TYPE_RAINSENSOR: str
TYPE_WEEKDAY: str

class RainMachineBinarySensorDescription(BinarySensorEntityDescription, RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey):
    def __init__(self, data_key, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CurrentRestrictionsBinarySensor(RainMachineEntity, BinarySensorEntity):
    entity_description: RainMachineBinarySensorDescription
    _attr_is_on: Incomplete
    def update_from_latest_data(self) -> None: ...

class ProvisionSettingsBinarySensor(RainMachineEntity, BinarySensorEntity):
    entity_description: RainMachineBinarySensorDescription
    _attr_is_on: Incomplete
    def update_from_latest_data(self) -> None: ...
