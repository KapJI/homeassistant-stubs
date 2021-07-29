from .entity import BlockAttributeDescription as BlockAttributeDescription, RestAttributeDescription as RestAttributeDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest
from .utils import is_momentary_input as is_momentary_input
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_OPENING as DEVICE_CLASS_OPENING, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE, DEVICE_CLASS_VIBRATION as DEVICE_CLASS_VIBRATION, STATE_ON as STATE_ON
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

SENSORS: Final[Any]
REST_SENSORS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyBinarySensor(ShellyBlockAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class ShellyRestBinarySensor(ShellyRestAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class ShellySleepingBinarySensor(ShellySleepingBlockAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
