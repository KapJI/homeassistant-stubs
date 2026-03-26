from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityState, InfraredInfo
from homeassistant.components.infrared import InfraredCommand as InfraredCommand, InfraredEntity as InfraredEntity
from homeassistant.core import callback as callback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

class EsphomeInfraredEntity(EsphomeEntity[InfraredInfo, EntityState], InfraredEntity):
    @callback
    def _on_device_update(self) -> None: ...
    @convert_api_error_ha_error
    async def async_send_command(self, command: InfraredCommand) -> None: ...

async_setup_entry: Incomplete
