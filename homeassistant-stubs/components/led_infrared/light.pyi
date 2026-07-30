from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LEDIrDeviceType as LEDIrDeviceType
from .entity import LEDIrBaseEntity as LEDIrBaseEntity
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.components.light import ATTR_EFFECT as ATTR_EFFECT, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
SUPPORTED_EFFECTS: Incomplete
SUPPORTED_COLORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LEDIrLightEntity(LEDIrBaseEntity, InfraredEmitterConsumerEntity, LightEntity):
    _attr_assumed_state: bool
    _attr_color_mode: Incomplete
    _attr_effect_list: list[str]
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _infrared_emitter_entity_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, device_type: LEDIrDeviceType, infrared_entity_id: str) -> None: ...
    _attr_is_on: bool
    _attr_effect: Incomplete
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _async_handle_event(self, event_type: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
