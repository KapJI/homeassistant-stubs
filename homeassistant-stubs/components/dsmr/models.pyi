from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription

class DSMRSensorEntityDescription(SensorEntityDescription):
    dsmr_versions: Union[set[str], None]
    is_gas: bool
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, dsmr_versions, is_gas) -> None: ...
