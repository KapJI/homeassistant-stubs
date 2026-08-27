from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudConfigEntry as SwitchbotCloudConfigEntry
from .const import BATTERY_CIRCULATOR_FAN_2_PRO_NIGHT_LIGHT_PARAMETERS_MAP as BATTERY_CIRCULATOR_FAN_2_PRO_NIGHT_LIGHT_PARAMETERS_MAP, NIGHT_LIGHT_BRIGHT as NIGHT_LIGHT_BRIGHT, NIGHT_LIGHT_ON as NIGHT_LIGHT_ON, NIGHT_LIGHT_SOFT as NIGHT_LIGHT_SOFT, STANDING_FAN_NIGHT_LIGHT_PARAMETERS_MAP as STANDING_FAN_NIGHT_LIGHT_PARAMETERS_MAP
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import override

async def async_setup_entry(hass: HomeAssistant, config: SwitchbotCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudStandingFanNightLight(SwitchBotCloudEntity, SelectEntity):
    _night_light_parameters_map: dict[str, str]
    _attr_entity_category: Incomplete
    _attr_current_option: str | None
    _attr_translation_key: str
    _attr_options: Incomplete
    @override
    async def async_select_option(self, option: str) -> None: ...
    @override
    def _set_attributes(self) -> None: ...

class SwitchBotCloudBatteryCirculatorFan2ProNightLight(SwitchBotCloudStandingFanNightLight):
    _night_light_parameters_map: dict[str, str]

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudStandingFanNightLight | SwitchBotCloudBatteryCirculatorFan2ProNightLight: ...
