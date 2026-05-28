from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, EntityState, InfraredInfo
from aioesphomeapi.client import InfraredRFReceiveEventModel as InfraredRFReceiveEventModel
from homeassistant.components.infrared import InfraredCommand as InfraredCommand, InfraredEmitterEntity as InfraredEmitterEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverEntity as InfraredReceiverEntity
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

class _EsphomeInfraredEntity(EsphomeEntity[InfraredInfo, EntityState]):
    @callback
    def _on_device_update(self) -> None: ...

class EsphomeInfraredEmitterEntity(_EsphomeInfraredEntity, InfraredEmitterEntity):
    @convert_api_error_ha_error
    async def async_send_command(self, command: InfraredCommand) -> None: ...

class EsphomeInfraredReceiverEntity(_EsphomeInfraredEntity, InfraredReceiverEntity):
    _unsub_receive: CALLBACK_TYPE | None
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _async_subscribe_receive(self) -> None: ...
    @callback
    def _on_device_update(self) -> None: ...
    @callback
    def _on_infrared_rf_receive(self, event: InfraredRFReceiveEventModel) -> None: ...

def _make_infrared_entity(entry_data: RuntimeEntryData, info: EntityInfo, state_type: type[EntityState]) -> _EsphomeInfraredEntity: ...

async_setup_entry: Incomplete
