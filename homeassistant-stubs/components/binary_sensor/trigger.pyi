from . import BinarySensorDeviceClass as BinarySensorDeviceClass, DOMAIN as DOMAIN
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.trigger import EntityTargetStateTriggerBase as EntityTargetStateTriggerBase, Trigger as Trigger
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType

def get_device_class_or_undefined(hass: HomeAssistant, entity_id: str) -> str | None | UndefinedType: ...

class BinarySensorOnOffTrigger(EntityTargetStateTriggerBase):
    _device_class: BinarySensorDeviceClass | None
    _domain: str
    def entity_filter(self, entities: set[str]) -> set[str]: ...

def make_binary_sensor_trigger(device_class: BinarySensorDeviceClass | None, to_state: str) -> type[BinarySensorOnOffTrigger]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
