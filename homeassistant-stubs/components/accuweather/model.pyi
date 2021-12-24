from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class AccuWeatherSensorDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, unit_metric, unit_imperial) -> None: ...
