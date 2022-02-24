from .const import ISY994_NODES as ISY994_NODES, ISY994_VARIABLES as ISY994_VARIABLES, UOM_DOUBLE_TEMP as UOM_DOUBLE_TEMP, UOM_FRIENDLY_NAME as UOM_FRIENDLY_NAME, UOM_INDEX as UOM_INDEX, UOM_ON_OFF as UOM_ON_OFF, UOM_TO_STATES as UOM_TO_STATES, _LOGGER as _LOGGER
from .entity import ISYEntity as ISYEntity, ISYNodeEntity as ISYNodeEntity
from .helpers import convert_isy_value_to_hass as convert_isy_value_to_hass, migrate_old_unique_ids as migrate_old_unique_ids
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYSensorEntity(ISYNodeEntity, SensorEntity):
    @property
    def raw_unit_of_measurement(self) -> Union[dict, str, None]: ...
    @property
    def native_value(self) -> Union[float, int, str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class ISYSensorVariableEntity(ISYEntity, SensorEntity):
    _name: Any
    def __init__(self, vname: str, vobj: object) -> None: ...
    @property
    def native_value(self) -> Union[float, int, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
