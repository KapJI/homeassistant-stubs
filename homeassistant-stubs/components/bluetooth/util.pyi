from .const import AdapterDetails as AdapterDetails, DEFAULT_ADAPTER_BY_PLATFORM as DEFAULT_ADAPTER_BY_PLATFORM, DEFAULT_ADDRESS as DEFAULT_ADDRESS, MACOS_DEFAULT_BLUETOOTH_ADAPTER as MACOS_DEFAULT_BLUETOOTH_ADAPTER, UNIX_DEFAULT_BLUETOOTH_ADAPTER as UNIX_DEFAULT_BLUETOOTH_ADAPTER, WINDOWS_DEFAULT_BLUETOOTH_ADAPTER as WINDOWS_DEFAULT_BLUETOOTH_ADAPTER
from homeassistant.core import callback as callback

async def async_get_bluetooth_adapters() -> dict[str, AdapterDetails]: ...
def async_default_adapter() -> str: ...
def adapter_human_name(adapter: str, address: str) -> str: ...
def adapter_unique_name(adapter: str, address: str) -> str: ...
async def async_reset_adapter(adapter: Union[str, None]) -> Union[bool, None]: ...
