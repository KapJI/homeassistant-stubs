from .const import DOMAIN as DOMAIN
from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, add_new_outputs as add_new_outputs
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from typing import Any

PARALLEL_UPDATES: int
STATE_REQUEST_DELAY: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusClimate(QbusEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_action: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_target_temperature_step: float
    _attr_preset_modes: list[str]
    _attr_preset_mode: str
    _request_state_debouncer: Debouncer | None
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    async def _state_received(self, msg: ReceiveMessage) -> None: ...
    def _set_hvac_action(self) -> None: ...
    async def _async_request_state(self) -> None: ...
