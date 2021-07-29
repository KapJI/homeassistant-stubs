from .const import DOMAIN as DOMAIN
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.climate import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntity as ClimateEntity, HVAC_MODE_HEAT as HVAC_MODE_HEAT, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloClimateDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, ClimateEntity):
    _attr_hvac_mode: Any
    _attr_hvac_modes: Any
    _attr_min_temp: Any
    _attr_max_temp: Any
    _attr_precision: Any
    _attr_supported_features: Any
    _attr_target_temperature_step: Any
    _attr_temperature_unit: Any
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    def set_hvac_mode(self, hvac_mode: str) -> None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
