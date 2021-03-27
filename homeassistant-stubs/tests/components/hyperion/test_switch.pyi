from . import call_registered_callback as call_registered_callback, create_mock_client as create_mock_client, setup_test_config_entry as setup_test_config_entry
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from typing import Any

TEST_COMPONENTS: Any
TEST_SWITCH_COMPONENT_BASE_ENTITY_ID: str
TEST_SWITCH_COMPONENT_ALL_ENTITY_ID: Any

async def test_switch_turn_on_off(hass: HomeAssistantType) -> None: ...
async def test_switch_has_correct_entities(hass: HomeAssistantType) -> None: ...
