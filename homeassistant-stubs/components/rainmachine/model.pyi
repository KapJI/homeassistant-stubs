from dataclasses import dataclass
from homeassistant.helpers.entity import EntityDescription as EntityDescription

@dataclass(frozen=True, kw_only=True)
class RainMachineEntityDescription(EntityDescription):
    api_category: str
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, api_category) -> None: ...
