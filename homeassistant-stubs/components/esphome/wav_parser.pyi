from _typeshed import Incomplete
from collections.abc import AsyncIterable, AsyncIterator

class WAVHeaderParser:
    expected_channels: Incomplete
    expected_width: Incomplete
    expected_sample_rate: Incomplete
    riff_checked: bool
    fmt_validated: bool
    data_bytes_remaining: int
    found_data: bool
    def __init__(self, expected_channels: int, expected_width: int, expected_sample_rate: int) -> None: ...
    def parse(self, bytes_buffer: bytearray) -> bool: ...

async def stream_wav(stream: AsyncIterable[bytes], *, expected_format: str = 'pcm', expected_channels: int, expected_width: int, expected_sample_rate: int, samples_per_chunk: int = 512) -> AsyncIterator[tuple[bytes, bool]]: ...
