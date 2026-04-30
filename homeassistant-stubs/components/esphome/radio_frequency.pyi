from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityState, RadioFrequencyInfo, RadioFrequencyModulation
from homeassistant.components.radio_frequency import RadioFrequencyTransmitterEntity as RadioFrequencyTransmitterEntity
from homeassistant.core import callback as callback
from rf_protocols import ModulationType, RadioFrequencyCommand as RadioFrequencyCommand

_LOGGER: Incomplete
PARALLEL_UPDATES: int
MODULATION_TYPE_TO_ESPHOME: dict[ModulationType, RadioFrequencyModulation]

class EsphomeRadioFrequencyEntity(EsphomeEntity[RadioFrequencyInfo, EntityState], RadioFrequencyTransmitterEntity):
    @property
    def supported_frequency_ranges(self) -> list[tuple[int, int]]: ...
    @callback
    def _on_device_update(self) -> None: ...
    @convert_api_error_ha_error
    async def async_send_command(self, command: RadioFrequencyCommand) -> None: ...

async_setup_entry: Incomplete
