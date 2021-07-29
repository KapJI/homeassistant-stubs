from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from typing import Callable

class GiosSensorEntityDescription(SensorEntityDescription):
    value: Union[Callable, None]
