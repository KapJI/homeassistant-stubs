from homeassistant.helpers import device_registry as dr, entity_registry as er

class PermissionLookup:
    entity_registry: er.EntityRegistry
    device_registry: dr.DeviceRegistry
    def __init__(self, entity_registry, device_registry) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
