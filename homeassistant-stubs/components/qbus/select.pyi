from .const import DOMAIN as DOMAIN
from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, create_new_entities as create_new_entities
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttStepperState
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusStepper(QbusEntity, SelectEntity):
    _state_cls = QbusMqttStepperState
    _attr_name: Incomplete
    _name_to_value: dict[str, int]
    _value_to_name: dict[int, str]
    _attr_options: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    @override
    async def _handle_state_received(self, state: QbusMqttStepperState) -> None: ...
