from _typeshed import Incomplete
from datetime import timedelta
from jwt import PyJWS, PyJWT
from typing import Any

class _PyJWSWithLoadCache(PyJWS):
    def _load(self, jwt: Union[str, bytes]) -> tuple[bytes, bytes, dict, bytes]: ...

class _PyJWTWithVerify(PyJWT):
    def decode_payload(self, jwt: str, key: str, options: dict[str, Any], algorithms: list[str]) -> dict[str, Any]: ...
    def verify_and_decode(self, jwt: str, key: str, algorithms: list[str], issuer: Union[str, None] = ..., leeway: Union[int, float, timedelta] = ..., options: Union[dict[str, Any], None] = ...) -> dict[str, Any]: ...

verify_and_decode: Incomplete
unverified_hs256_token_decode: Incomplete
