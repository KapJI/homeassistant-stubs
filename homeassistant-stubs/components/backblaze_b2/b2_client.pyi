from b2sdk.v2 import B2Api as BaseB2Api, InMemoryAccountInfo as InMemoryAccountInfo
from b2sdk.v2.b2http import B2Http as BaseB2Http
from b2sdk.v2.session import B2Session as BaseB2Session

__all__ = ['B2Api', 'InMemoryAccountInfo']

class B2Http(BaseB2Http):
    CONNECTION_TIMEOUT = CONNECTION_TIMEOUT
    TIMEOUT_FOR_UPLOAD = TIMEOUT_FOR_UPLOAD

class B2Session(BaseB2Session):
    B2HTTP_CLASS = B2Http

class B2Api(BaseB2Api):
    SESSION_CLASS = B2Session
