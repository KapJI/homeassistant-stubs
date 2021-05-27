from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, DOMAIN as DOMAIN, SENSOR_TYPE_SENSED as SENSOR_TYPE_SENSED
from .model import DeviceComponentDescription as DeviceComponentDescription
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

DEVICE_BINARY_SENSORS: dict[str, list[DeviceComponentDescription]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub) -> list[OneWireBaseEntity]: ...

class OneWireProxyBinarySensor(OneWireProxyEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
