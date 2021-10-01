from collections.abc import Callable as Callable
from forecast_solar.models import Estimate as Estimate
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from typing import Any

class ForecastSolarSensorEntityDescription(SensorEntityDescription):
    state: Union[Callable[[Estimate], Any], None]
