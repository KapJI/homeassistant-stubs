from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class GiosSensorEntityDescription(SensorEntityDescription):
    value: Union[Callable, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, value) -> None: ...
