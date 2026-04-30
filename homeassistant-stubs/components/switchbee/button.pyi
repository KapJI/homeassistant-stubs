from .coordinator import SwitchBeeConfigEntry as SwitchBeeConfigEntry
from .entity import SwitchBeeEntity as SwitchBeeEntity
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: SwitchBeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBeeButton(SwitchBeeEntity, ButtonEntity):
    async def async_press(self) -> None: ...
