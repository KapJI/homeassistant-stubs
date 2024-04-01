from homeassistant.components.number import NumberEntityDescription as NumberEntityDescription
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.const import Platform as Platform
from myuplink import DevicePoint as DevicePoint

def find_matching_platform(device_point: DevicePoint, description: SensorEntityDescription | NumberEntityDescription | None = None) -> Platform: ...
def skip_entity(model: str, device_point: DevicePoint) -> bool: ...
