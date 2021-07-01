class ForecastSolarSensor:
    key: str
    name: str
    device_class: Union[str, None]
    entity_registry_enabled_default: bool
    state_class: Union[str, None]
    unit_of_measurement: Union[str, None]
