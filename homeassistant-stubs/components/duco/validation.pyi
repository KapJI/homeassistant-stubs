from _typeshed import Incomplete
from duco_connectivity import DucoClient as DucoClient
from duco_connectivity.models import BoardInfo as BoardInfo

_MIN_PUBLIC_API_VERSION: Incomplete

class UnsupportedBoardError(Exception): ...

def validate_board_support(board_info: BoardInfo) -> None: ...
async def async_get_supported_board_info(client: DucoClient) -> BoardInfo: ...
