from collections.abc import Callable as Callable
from forecast_solar.models import Estimate as Estimate
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from typing import Any

class ForecastSolarSensorEntityDescription(SensorEntityDescription):
    state: Union[Callable[[Estimate], Any], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, state) -> None: ...
