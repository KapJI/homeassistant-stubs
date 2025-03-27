from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import BSH_AMBIENT_LIGHT_COLOR_CUSTOM_COLOR as BSH_AMBIENT_LIGHT_COLOR_CUSTOM_COLOR, DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .entity import HomeConnectEntity as HomeConnectEntity
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.model import SettingKey
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HomeConnectLightEntityDescription(LightEntityDescription):
    brightness_key: SettingKey | None = ...
    color_key: SettingKey | None = ...
    enable_custom_color_value_key: str | None = ...
    custom_color_key: SettingKey | None = ...
    brightness_scale: tuple[float, float] = ...

LIGHTS: tuple[HomeConnectLightEntityDescription, ...]

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectLight(HomeConnectEntity, LightEntity):
    entity_description: LightEntityDescription
    _brightness_key: Incomplete
    _custom_color_key: Incomplete
    _color_key: Incomplete
    _enable_custom_color_value_key: Incomplete
    _brightness_scale: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: HomeConnectLightEntityDescription) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_rgb_color: Incomplete
    _attr_hs_color: Incomplete
    def update_native_value(self) -> None: ...
