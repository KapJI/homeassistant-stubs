from typing import Any

_LOGGER: Any

def is_virtual_env() -> bool: ...
def is_docker_env() -> bool: ...
def is_installed(package: str) -> bool: ...
def install_package(package: str, upgrade: bool = ..., target: Union[str, None] = ..., constraints: Union[str, None] = ..., find_links: Union[str, None] = ..., timeout: Union[int, None] = ..., no_cache_dir: Union[bool, None] = ...) -> bool: ...
async def async_get_user_site(deps_dir: str) -> str: ...
