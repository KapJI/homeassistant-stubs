from . import MarantzIrConfigEntry as MarantzIrConfigEntry
from .const import DOMAIN as DOMAIN, MODELS as MODELS
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from infrared_protocols.codes.marantz.audio import MarantzAudioCode as MarantzAudioCode

class MarantzIrEntity(InfraredEmitterConsumerEntity):
    _attr_has_entity_name: bool
    _infrared_emitter_entity_id: Incomplete
    _runtime_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: MarantzIrConfigEntry, infrared_entity_id: str, unique_id_suffix: str) -> None: ...
    async def _send_marantz_command(self, code: MarantzAudioCode, repeat_count: int = 0) -> None: ...
