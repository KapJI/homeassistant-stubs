from aiohttp import web_protocol

class CancelOnDisconnectRequestHandler(web_protocol.RequestHandler):
    def connection_lost(self, exc: Union[BaseException, None]) -> None: ...

def restore_original_aiohttp_cancel_behavior() -> None: ...