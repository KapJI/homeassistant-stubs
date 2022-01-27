from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, DEVICE_KEYS_0_3 as DEVICE_KEYS_0_3, DEVICE_KEYS_0_7 as DEVICE_KEYS_0_7, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B, DOMAIN as DOMAIN, READ_MODE_BOOL as READ_MODE_BOOL
from .model import OWServerDeviceDescription as OWServerDeviceDescription
from .onewire_entities import OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class OneWireBinarySensorEntityDescription(OneWireEntityDescription, BinarySensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, read_mode) -> None: ...

DEVICE_BINARY_SENSORS: dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]
HOBBYBOARD_EF: dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub) -> list[BinarySensorEntity]: ...

class OneWireProxyBinarySensor(OneWireProxyEntity, BinarySensorEntity):
    entity_description: OneWireBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
