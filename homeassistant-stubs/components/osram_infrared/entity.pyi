from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from infrared_protocols.codes.osram.light import OsramLightCode as OsramLightCode

FULL_FRAME_REPEAT_DELAY: float

class OsramIrEntity(Entity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...

class OsramIrEmitterEntity(OsramIrEntity, InfraredEmitterConsumerEntity):
    _infrared_emitter_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str) -> None: ...
    async def _async_send_code(self, code: OsramLightCode, *, repeat_count: int = 1) -> None: ...
