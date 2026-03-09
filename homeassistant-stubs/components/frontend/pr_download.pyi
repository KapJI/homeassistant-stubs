import pathlib
from _typeshed import Incomplete
from aiogithubapi import GitHubAPI
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
GITHUB_REPO: str
ARTIFACT_NAME: str
MAX_ZIP_FILES: int
MAX_ZIP_SIZE: Incomplete
ERROR_INVALID_TOKEN: str
ERROR_RATE_LIMIT: str

async def _get_pr_shas(client: GitHubAPI, pr_number: int) -> tuple[str, str]: ...
async def _find_pr_artifact(client: GitHubAPI, pr_number: int, head_sha: str) -> str: ...
async def _download_artifact_data(hass: HomeAssistant, artifact_url: str, github_token: str) -> bytes: ...
def _extract_artifact(artifact_data: bytes, cache_dir: pathlib.Path, cache_key: str) -> None: ...
async def download_pr_artifact(hass: HomeAssistant, pr_number: int, github_token: str, tmp_dir: pathlib.Path) -> pathlib.Path: ...
