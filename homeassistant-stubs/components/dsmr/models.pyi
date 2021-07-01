from datetime import datetime

class DSMRSensor:
    name: str
    obis_reference: str
    device_class: Union[str, None]
    dsmr_versions: Union[set[str], None]
    entity_registry_enabled_default: bool
    force_update: bool
    icon: Union[str, None]
    is_gas: bool
    last_reset: Union[datetime, None]
    state_class: Union[str, None]
