from typing import TypedDict

class EntityInfo(TypedDict):
    name: str
    entity_id: str
    unit_of_measurement: Union[str, None]
    device_class: Union[str, None]

class ClimateExtraAttributes(TypedDict):
    battery_low: bool
    device_locked: bool
    locked: bool
    battery_level: int
    holiday_mode: bool
    summer_mode: bool
    window_open: bool

class SensorExtraAttributes(TypedDict):
    device_locked: bool
    locked: bool

class SwitchExtraAttributes(TypedDict):
    device_locked: bool
    locked: bool
    total_consumption: str
    total_consumption_unit: str
    temperature: str
    temperature_unit: str
