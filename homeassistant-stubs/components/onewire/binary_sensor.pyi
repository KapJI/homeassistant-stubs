from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, DOMAIN as DOMAIN, READ_MODE_BOOL as READ_MODE_BOOL
from .onewire_entities import OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class OneWireBinarySensorEntityDescription(OneWireEntityDescription, BinarySensorEntityDescription): ...

DEVICE_BINARY_SENSORS: dict[str, tuple[OneWireBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub) -> list[BinarySensorEntity]: ...

class OneWireProxyBinarySensor(OneWireProxyEntity, BinarySensorEntity):
    entity_description: OneWireBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
