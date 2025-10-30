from .const import DEVICE_KEYS_0_3 as DEVICE_KEYS_0_3, DEVICE_KEYS_0_7 as DEVICE_KEYS_0_7, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B
from .entity import OneWireEntity as OneWireEntity
from .onewirehub import OWDeviceDescription as OWDeviceDescription, OneWireConfigEntry as OneWireConfigEntry, OneWireHub as OneWireHub, SIGNAL_NEW_DEVICE_CONNECTED as SIGNAL_NEW_DEVICE_CONNECTED
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete
DEVICE_SWITCHES: dict[str, tuple[SwitchEntityDescription, ...]]
HOBBYBOARD_EF: dict[str, tuple[SwitchEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, tuple[SwitchEntityDescription, ...]]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def get_entities(onewire_hub: OneWireHub, devices: list[OWDeviceDescription]) -> list[OneWireSwitchEntity]: ...

class OneWireSwitchEntity(OneWireEntity, SwitchEntity):
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
