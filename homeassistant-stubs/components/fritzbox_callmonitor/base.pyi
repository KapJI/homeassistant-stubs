from .const import REGEX_NUMBER as REGEX_NUMBER, UNKNOWN_NAME as UNKNOWN_NAME
from fritzconnection.lib.fritzphonebook import FritzPhonebook
from homeassistant.util import Throttle as Throttle
from typing import Any

_LOGGER: Any
MIN_TIME_PHONEBOOK_UPDATE: Any

class FritzBoxPhonebook:
    fph: FritzPhonebook
    phonebook_dict: dict[str, list[str]]
    number_dict: dict[str, str]
    host: Any
    username: Any
    password: Any
    phonebook_id: Any
    prefixes: Any
    def __init__(self, host: str, username: str, password: str, phonebook_id: Union[int, None] = ..., prefixes: Union[list[str], None] = ...) -> None: ...
    def init_phonebook(self) -> None: ...
    def update_phonebook(self) -> None: ...
    def get_phonebook_ids(self) -> list[int]: ...
    def get_name(self, number: str) -> str: ...
