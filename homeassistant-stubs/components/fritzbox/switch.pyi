from . import FritzBoxEntity as FritzBoxEntity
from .const import ATTR_STATE_DEVICE_LOCKED as ATTR_STATE_DEVICE_LOCKED, ATTR_STATE_LOCKED as ATTR_STATE_LOCKED, ATTR_TEMPERATURE_UNIT as ATTR_TEMPERATURE_UNIT, ATTR_TOTAL_CONSUMPTION as ATTR_TOTAL_CONSUMPTION, ATTR_TOTAL_CONSUMPTION_UNIT as ATTR_TOTAL_CONSUMPTION_UNIT, CONF_COORDINATOR as CONF_COORDINATOR
from .model import SwitchExtraAttributes as SwitchExtraAttributes
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_TOTAL_CONSUMPTION_UNIT_VALUE = ENERGY_KILO_WATT_HOUR

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxSwitch(FritzBoxEntity, SwitchEntity):
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> SwitchExtraAttributes: ...
    @property
    def current_power_w(self) -> float: ...
