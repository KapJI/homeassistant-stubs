from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity, WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywemo import Insight, Maker

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WemoBinarySensor(WemoBinaryStateEntity, BinarySensorEntity): ...

class MakerBinarySensor(WemoEntity, BinarySensorEntity):
    _name_suffix: str
    wemo: Maker
    @property
    def is_on(self) -> bool: ...

class InsightBinarySensor(WemoBinarySensor):
    _name_suffix: str
    wemo: Insight
    @property
    def is_on(self) -> bool: ...
