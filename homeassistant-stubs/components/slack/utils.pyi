from _typeshed import Incomplete
from slack_sdk.web.async_client import AsyncWebClient as AsyncWebClient

_LOGGER: Incomplete

async def upload_file_to_slack(client: AsyncWebClient, channel_ids: list[str | None], file_content: bytes | str | None, filename: str, title: str | None, message: str, thread_ts: str | None, file_path: str | None = None) -> None: ...
