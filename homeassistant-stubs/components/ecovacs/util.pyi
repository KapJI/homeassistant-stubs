from .controller import EcovacsController as EcovacsController
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity

def get_client_device_id() -> str: ...
def get_supported_entitites(controller: EcovacsController, entity_class: type[EcovacsDescriptionEntity], descriptions: tuple[EcovacsCapabilityEntityDescription, ...]) -> list[EcovacsEntity]: ...
