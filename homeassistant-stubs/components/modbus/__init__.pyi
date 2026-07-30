from .const import DOMAIN as DOMAIN
from .modbus import DATA_MODBUS_HUBS as DATA_MODBUS_HUBS, ModbusHub as ModbusHub, async_modbus_setup as async_modbus_setup
from .schemas import CONFIG_SCHEMA as CONFIG_SCHEMA
from _typeshed import Incomplete
from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.entity_platform import async_get_platforms as async_get_platforms
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete

def get_hub(hass: HomeAssistant, name: str) -> ModbusHub: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
