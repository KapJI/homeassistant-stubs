from homeassistant.helpers.entity import EntityDescription as EntityDescription

class RainMachineEntityDescriptionMixinApiCategory:
    api_category: str
    def __init__(self, api_category) -> None: ...

class RainMachineEntityDescriptionMixinDataKey:
    data_key: str
    def __init__(self, data_key) -> None: ...

class RainMachineEntityDescriptionMixinUid:
    uid: int
    def __init__(self, uid) -> None: ...

class RainMachineEntityDescription(EntityDescription, RainMachineEntityDescriptionMixinApiCategory):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...
