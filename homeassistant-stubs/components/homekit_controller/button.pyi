from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import CharacteristicEntity as CharacteristicEntity
from aiohomekit.model.characteristics import Characteristic as Characteristic
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

class HomeKitButtonEntityDescription(ButtonEntityDescription):
    write_value: Union[int, str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, write_value) -> None: ...

BUTTON_ENTITIES: dict[str, HomeKitButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeKitButton(CharacteristicEntity, ButtonEntity):
    entity_description: HomeKitButtonEntityDescription
    def __init__(self, conn: HKDevice, info: ConfigType, char: Characteristic, description: HomeKitButtonEntityDescription) -> None: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str: ...
    async def async_press(self) -> None: ...

class HomeKitEcobeeClearHoldButton(CharacteristicEntity, ButtonEntity):
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def name(self) -> str: ...
    async def async_press(self) -> None: ...

BUTTON_ENTITY_CLASSES: dict[str, type]
