from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, DOMAIN as DOMAIN, SWITCH_TYPE_LATCH as SWITCH_TYPE_LATCH, SWITCH_TYPE_PIO as SWITCH_TYPE_PIO
from .model import DeviceComponentDescription as DeviceComponentDescription
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DEVICE_SWITCHES: dict[str, list[DeviceComponentDescription]]
LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub) -> list[OneWireBaseEntity]: ...

class OneWireProxySwitch(OneWireProxyEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
