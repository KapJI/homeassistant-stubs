from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from typing import Callable

class AirlySensorEntityDescription(SensorEntityDescription):
    value: Callable
