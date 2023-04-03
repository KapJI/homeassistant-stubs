from .const import REGEX_NUMBER as REGEX_NUMBER, UNKNOWN_NAME as UNKNOWN_NAME
from _typeshed import Incomplete
from fritzconnection.lib.fritzphonebook import FritzPhonebook
from homeassistant.util import Throttle as Throttle

_LOGGER: Incomplete
MIN_TIME_PHONEBOOK_UPDATE: Incomplete

class FritzBoxPhonebook:
    fph: FritzPhonebook
    phonebook_dict: dict[str, list[str]]
    number_dict: dict[str, str]
    host: Incomplete
    username: Incomplete
    password: Incomplete
    phonebook_id: Incomplete
    prefixes: Incomplete
    def __init__(self, host: str, username: str, password: str, phonebook_id: int | None = ..., prefixes: list[str] | None = ...) -> None: ...
    def init_phonebook(self) -> None: ...
    def update_phonebook(self) -> None: ...
    def get_phonebook_ids(self) -> list[int]: ...
    def get_name(self, number: str) -> str: ...
