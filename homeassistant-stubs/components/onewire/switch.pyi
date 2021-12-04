from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, DEVICE_KEYS_0_7 as DEVICE_KEYS_0_7, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B, DOMAIN as DOMAIN, READ_MODE_BOOL as READ_MODE_BOOL
from .onewire_entities import OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.onewire.model import OWServerDeviceDescription as OWServerDeviceDescription
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class OneWireSwitchEntityDescription(OneWireEntityDescription, SwitchEntityDescription): ...

DEVICE_SWITCHES: dict[str, tuple[OneWireEntityDescription, ...]]
LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub) -> list[SwitchEntity]: ...

class OneWireProxySwitch(OneWireProxyEntity, SwitchEntity):
    entity_description: OneWireSwitchEntityDescription
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
