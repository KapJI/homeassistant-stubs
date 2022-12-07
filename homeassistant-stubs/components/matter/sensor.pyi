from .adapter import MatterAdapter as MatterAdapter
from .const import DOMAIN as DOMAIN
from .entity import MatterEntity as MatterEntity, MatterEntityDescriptionBaseClass as MatterEntityDescriptionBaseClass
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from chip.clusters.Types import Nullable as Nullable
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR as VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.common.models import device_types
from matter_server.common.models.device_type_instance import MatterDeviceTypeInstance as MatterDeviceTypeInstance
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterSensor(MatterEntity, SensorEntity):
    _attr_state_class: Incomplete
    entity_description: MatterSensorEntityDescription
    _attr_native_value: Incomplete
    def _update_from_device(self) -> None: ...

def _get_attribute_value(device_type_instance: MatterDeviceTypeInstance, attribute: clusters.ClusterAttributeDescriptor) -> Any: ...

class MatterSensorEntityDescriptionMixin:
    measurement_to_ha: Callable[[float], float]
    def __init__(self, measurement_to_ha) -> None: ...

class MatterSensorEntityDescription(SensorEntityDescription, MatterEntityDescriptionBaseClass, MatterSensorEntityDescriptionMixin):
    def __init__(self, measurement_to_ha, entity_cls, subscribe_attributes, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

MatterSensorEntityDescriptionFactory: Incomplete
DEVICE_ENTITY: dict[type[device_types.DeviceType], Union[MatterEntityDescriptionBaseClass, list[MatterEntityDescriptionBaseClass]]]
