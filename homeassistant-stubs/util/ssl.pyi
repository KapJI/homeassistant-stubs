import ssl
from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum

class SSLCipherList(StrEnum):
    PYTHON_DEFAULT: str
    INTERMEDIATE: str
    MODERN: str

SSL_CIPHER_LISTS: Incomplete

def create_no_verify_ssl_context(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...
def client_context(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...

_DEFAULT_SSL_CONTEXT: Incomplete
_DEFAULT_NO_VERIFY_SSL_CONTEXT: Incomplete

def get_default_context() -> ssl.SSLContext: ...
def get_default_no_verify_context() -> ssl.SSLContext: ...
def server_context_modern() -> ssl.SSLContext: ...
def server_context_intermediate() -> ssl.SSLContext: ...
