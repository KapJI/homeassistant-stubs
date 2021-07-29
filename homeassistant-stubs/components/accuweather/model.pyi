from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class AccuWeatherSensorDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
