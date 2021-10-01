from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class GiosSensorEntityDescription(SensorEntityDescription):
    value: Union[Callable, None]
