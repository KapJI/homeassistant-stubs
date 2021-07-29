from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class DSMRSensorEntityDescription(SensorEntityDescription):
    dsmr_versions: Union[set[str], None]
    is_gas: bool
