from .const import LOGGER as LOGGER, PLATFORMS as PLATFORMS
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage, async_prepare_subscribe_topics as async_prepare_subscribe_topics, async_subscribe_topics as async_subscribe_topics, async_unsubscribe_topics as async_unsubscribe_topics
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from inelsmqtt import InelsMqtt
from inelsmqtt.devices import Device as Device

type InelsConfigEntry = ConfigEntry[InelsData]
@dataclass
class InelsData:
    mqtt: InelsMqtt
    devices: list[Device]

async def async_setup_entry(hass: HomeAssistant, entry: InelsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: InelsConfigEntry) -> bool: ...
