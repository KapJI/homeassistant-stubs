from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from tests.common import MockConfigEntry as MockConfigEntry
from types import TracebackType
from typing import Any, Dict, Optional, Type
from unittest.mock import AsyncMock, Mock

TEST_HOST: str
TEST_PORT: Any
TEST_PORT_UI: Any
TEST_INSTANCE: int
TEST_ID: str
TEST_SYSINFO_ID: str
TEST_SYSINFO_VERSION: str
TEST_PRIORITY: int
TEST_ENTITY_ID_1: str
TEST_ENTITY_ID_2: str
TEST_ENTITY_ID_3: str
TEST_PRIORITY_LIGHT_ENTITY_ID_1: str
TEST_TITLE: Any
TEST_TOKEN: str
TEST_CONFIG_ENTRY_ID: str
TEST_CONFIG_ENTRY_OPTIONS: Dict[str, Any]
TEST_INSTANCE_1: Dict[str, Any]
TEST_INSTANCE_2: Dict[str, Any]
TEST_INSTANCE_3: Dict[str, Any]
TEST_AUTH_REQUIRED_RESP: Dict[str, Any]
TEST_AUTH_NOT_REQUIRED_RESP: Any

class AsyncContextManagerMock(Mock):
    async def __aenter__(self) -> Optional[AsyncContextManagerMock]: ...
    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...

def create_mock_client() -> Mock: ...
def add_test_config_entry(hass: HomeAssistantType, data: Optional[Dict[str, Any]]=...) -> ConfigEntry: ...
async def setup_test_config_entry(hass: HomeAssistantType, config_entry: Optional[ConfigEntry]=..., hyperion_client: Optional[Mock]=...) -> ConfigEntry: ...
def call_registered_callback(client: AsyncMock, key: str, *args: Any, **kwargs: Any) -> None: ...
