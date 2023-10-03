from .const import CONF_DATA_TYPE as CONF_DATA_TYPE, CONF_DEVICE_ADDRESS as CONF_DEVICE_ADDRESS, CONF_INPUT_TYPE as CONF_INPUT_TYPE, CONF_SLAVE_COUNT as CONF_SLAVE_COUNT, CONF_SWAP as CONF_SWAP, CONF_SWAP_BYTE as CONF_SWAP_BYTE, CONF_SWAP_NONE as CONF_SWAP_NONE, CONF_SWAP_WORD as CONF_SWAP_WORD, CONF_SWAP_WORD_BYTE as CONF_SWAP_WORD_BYTE, CONF_VIRTUAL_COUNT as CONF_VIRTUAL_COUNT, CONF_WRITE_TYPE as CONF_WRITE_TYPE, DEFAULT_HUB as DEFAULT_HUB, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DataType as DataType, PLATFORMS as PLATFORMS, SERIAL as SERIAL
from _typeshed import Incomplete
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_COMMAND_OFF as CONF_COMMAND_OFF, CONF_COMMAND_ON as CONF_COMMAND_ON, CONF_COUNT as CONF_COUNT, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SLAVE as CONF_SLAVE, CONF_STRUCTURE as CONF_STRUCTURE, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TYPE as CONF_TYPE
from typing import Any, NamedTuple

_LOGGER: Incomplete

class ENTRY(NamedTuple):
    struct_id: Incomplete
    register_count: Incomplete
    validate_parm: Incomplete

class PARM_IS_LEGAL(NamedTuple):
    count: Incomplete
    structure: Incomplete
    slave_count: Incomplete
    swap_byte: Incomplete
    swap_word: Incomplete

DEFAULT_STRUCT_FORMAT: Incomplete

def struct_validator(config: dict[str, Any]) -> dict[str, Any]: ...
def number_validator(value: Any) -> int | float: ...
def nan_validator(value: Any) -> int: ...
def scan_interval_validator(config: dict) -> dict: ...
def duplicate_entity_validator(config: dict) -> dict: ...
def duplicate_modbus_validator(config: list) -> list: ...
