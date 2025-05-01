from aiohttp.web import Application as Application, Request as Request, StreamResponse as StreamResponse
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from multidict import istr
from typing import Final

REFERRER_POLICY: Final[istr]
X_CONTENT_TYPE_OPTIONS: Final[istr]
X_FRAME_OPTIONS: Final[istr]

@callback
def setup_headers(app: Application, use_x_frame_options: bool) -> None: ...
