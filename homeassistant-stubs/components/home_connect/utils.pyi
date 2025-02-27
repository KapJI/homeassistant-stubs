from _typeshed import Incomplete
from aiohomeconnect.model.error import HomeConnectError as HomeConnectError

RE_CAMEL_CASE: Incomplete

def get_dict_from_home_connect_error(err: HomeConnectError) -> dict[str, str]: ...
def bsh_key_to_translation_key(bsh_key: str) -> str: ...
