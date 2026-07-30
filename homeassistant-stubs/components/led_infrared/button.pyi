from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LEDIrDeviceType as LEDIrDeviceType
from .entity import LEDIrBaseEntity as LEDIrBaseEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
SUPPORTED_BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LEDIrButtonEntity(LEDIrBaseEntity, InfraredEmitterConsumerEntity, ButtonEntity):
    _infrared_emitter_entity_id: Incomplete
    _attr_unique_id: Incomplete
    _key: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, entry: ConfigEntry, device_type: LEDIrDeviceType, infrared_entity_id: str, key: str) -> None: ...
    @override
    async def async_press(self) -> None: ...
